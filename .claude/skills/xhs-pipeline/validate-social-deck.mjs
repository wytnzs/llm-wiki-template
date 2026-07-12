#!/usr/bin/env node

/**
 * validate-social-deck.mjs
 * 小红书卡片校验脚本
 * 检查：溢出(R1)、底部栏碰撞(R2)、最小字号(R4)、四横带密度(R5)
 *
 * 使用: node validate-social-deck.mjs <task-dir>
 * 需要 Playwright 依赖
 */

import { chromium } from 'playwright';
import { readFileSync, existsSync } from 'fs';
import { join, resolve } from 'path';

const taskDir = process.argv[2] || '.';
const htmlPath = resolve(taskDir, 'index.html');

if (!existsSync(htmlPath)) {
  console.error(`❌ 未找到 index.html: ${htmlPath}`);
  process.exit(1);
}

const W = 1080, H = 1440;
let passed = 0, failed = 0, warnings = 0;

function check(rule, condition, detail) {
  if (condition) {
    console.log(`  ✅ ${rule}: ${detail}`);
    passed++;
  } else {
    console.log(`  ❌ ${rule}: ${detail}`);
    failed++;
  }
}

function warn(rule, detail) {
  console.log(`  ⚠️  ${rule}: ${detail}`);
  warnings++;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 1600 } });

  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  // 额外等待字体加载 + WebGL 渲染
  await page.waitForTimeout(1500);

  const posters = await page.$$('.poster.xhs');
  if (posters.length === 0) {
    console.log('⚠️  未找到任何 .poster.xhs 元素');
  }

  console.log(`\n📋 共 ${posters.length} 张卡片\n`);

  for (let i = 0; i < posters.length; i++) {
    const el = posters[i];
    console.log(`--- 卡片 ${i + 1} ---`);

    // R1: 溢出检查
    const overflow = await el.evaluate(el => {
      const cs = getComputedStyle(el);
      return cs.overflow === 'visible' || cs.overflowX === 'visible' || cs.overflowY === 'visible';
    });
    check('R1 溢出', !overflow, `overflow 已隐藏`);

    // 尺寸检查
    const box = await el.boundingBox();
    if (box) {
      check('尺寸宽', Math.abs(box.width - W) < 5, `${Math.round(box.width)}px ≈ ${W}px`);
      check('尺寸高', Math.abs(box.height - H) < 5, `${Math.round(box.height)}px ≈ ${H}px`);
    }

    // R4: 最小字号检查（查找 < 18px 的文本元素）
    const smallTexts = await el.evaluate(el => {
      const all = el.querySelectorAll('*');
      const results = [];
      for (const node of all) {
        const cs = getComputedStyle(node);
        const size = parseFloat(cs.fontSize);
        if (size > 0 && size < 18 && node.textContent.trim().length > 0) {
          results.push({ tag: node.tagName, size, text: node.textContent.trim().slice(0, 30) });
        }
      }
      return results;
    });
    if (smallTexts.length > 0) {
      warn('R4 最小字号', `${smallTexts.length} 处文本 < 18px: ${smallTexts.map(t => `${t.tagName} ${t.size}px "${t.text}"`).join(', ')}`);
    } else {
      check('R4 最小字号', true, '所有文本 ≥ 18px');
    }

    // R5: 四横带密度检查（内容是否填满 75% 画布）
    const density = await el.evaluate(el => {
      const children = el.querySelector('.content');
      if (!children) return 0;
      const contentRect = children.getBoundingClientRect();
      const parentRect = el.getBoundingClientRect();
      return (contentRect.height / parentRect.height) * 100;
    });
    if (density < 75) {
      warn('R5 密度', `内容覆盖 ${Math.round(density)}% 画布（需 ≥75%）`);
    } else {
      check('R5 密度', true, `内容覆盖 ${Math.round(density)}% 画布`);
    }

    // R2: 底部栏碰撞（检查 issue-strip 或类似元数据是否在底部 60px 内）
    const bottomCollision = await el.evaluate(el => {
      const strips = el.querySelectorAll('.issue-strip, .chrome-min, .t-meta');
      const elRect = el.getBoundingClientRect();
      for (const s of strips) {
        const sRect = s.getBoundingClientRect();
        if (sRect.bottom > elRect.bottom) return true;
      }
      return false;
    });
    check('R2 底部碰撞', !bottomCollision, '元数据未超出画布底部');
  }

  console.log(`\n===== 汇总 =====`);
  console.log(`✅ 通过: ${passed}`);
  console.log(`❌ 失败: ${failed}`);
  console.log(`⚠️  警告: ${warnings}`);

  await browser.close();
  process.exit(failed > 0 ? 1 : 0);
})();
