---
name: style-brief-pipeline
description: Generate and apply style briefs for content production. Use when creating, rewriting, adapting, publishing, or repurposing content for WeChat Official Account, Xiaohongshu, short video, social cards, article layout, visual design, image prompts, chart beautification, or when the user asks for 审美风格, 写作风格, 公众号排版, 小红书卡片, 配图, 图片美化, 风格规范, 私有内容引擎, or 可分享规范.
---

# Style Brief Pipeline

Create a `style-brief` after `content-brief` and before platform production.

`content-brief` answers: what to say, why it is credible, and what sources support it.
`style-brief` answers: who is speaking, how it should feel, which platform form to use, and what visual assets are needed.

## Workflow

1. Read the current `content-brief` if available. If not, infer the minimum topic, target reader, core viewpoint, platform, and risk boundary from the user's request.
2. Decide whether the task is private production or shareable-template production.
3. Read the relevant reference:
   - Private production: `references/private-style-system.md`
   - Shareable template/spec: `references/shareable-style-system.md`
   - Platform and theme routing: `references/visual-routing.md`
   - Image, chart, and social-card visuals: `references/image-system.md`
   - JSON field definitions: `references/style-brief-schema.md`
4. Produce or update `.claude/drafts/style-brief.json` using `.claude/drafts/style-brief.template.json`.
5. Route output:
   - WeChat long article: choose one article theme and one image strategy.
   - Xiaohongshu carousel: choose a card structure, cover hook, and central visual.
   - Short video: choose tone, opening tension, scene vocabulary, and visual cue list.
6. Run a quality pass before handoff: identity consistency, platform fit, visual clarity, legal/claim safety, and shareability.

## Private vs Shareable

Use private mode by default for the owner of this knowledge base.

Private mode may use the owner's expression DNA, point-of-view strength, preferred openings, endings, forbidden phrases, and personal content rhythm.

Use shareable mode when the user asks to publish, share, teach, open-source, productize, or provide a template for others.

Shareable mode must not copy the owner's voice. Provide selectors, variables, checklists, and blank fields that help another creator define their own style.

## Output Rules

- Do not merge `content-brief` and `style-brief`. Keep source/claim logic separate from expression/visual logic.
- Do not create many free-floating themes. Keep one mother style and a small number of routed variants.
- Do not let visual decoration weaken accuracy. For insurance, legal, finance, and data content, credibility outranks prettiness.
- Do not copy third-party component code or prompts directly into public shareable materials. Re-express the method and build original local specifications.
- If exact platform dimensions are required, verify the current platform requirement before hardcoding sizes.

## Default Style System

For this knowledge base, default to:

`restrained knowledge editorial + material explainer visuals`

Use three routed variants:

1. Deep editorial: WeChat long-form观点、趋势、方法论、案例拆解.
2. Dense tutorial: WeChat教程、清单、工具盘点、操作指南.
3. Material explainer: Xiaohongshu cover, carousel center image, chart beautification, and social-card visuals.

## Quality Gate

Before delivering a style decision or production artifact, check:

- Does it still sound like the intended speaker?
- Is the platform form appropriate instead of mechanically reused?
- Are color, typography, spacing, and image language consistent?
- Does each visual explain one idea rather than decorate the page?
- Are all claims safely bounded, especially for insurance and disputes?
- Could a shareable version let another person define their own voice instead of copying this one?
