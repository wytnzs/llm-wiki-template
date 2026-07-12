# Style Brief Schema

Use `.claude/drafts/style-brief.template.json` as the writable template.

## Field Guide

| Field | Meaning |
|---|---|
| `mode` | `private` or `shareable` |
| `source_content_brief` | path to the content brief used |
| `platforms` | target platforms |
| `mother_style` | stable account-level style |
| `route` | selected style route for this content |
| `voice_profile` | tone, stance, rhythm, taboo expressions |
| `visual_profile` | colors, typography mood, layout density, image language |
| `image_plan` | required images, chart treatment, prompt direction |
| `platform_plan` | WeChat/Xiaohongshu/video-specific output decisions |
| `shareable_controls` | fields to expose when making a public template |
| `quality_gate` | checks required before final production |

## Generation Rules

- Fill private fields only in private mode.
- In shareable mode, replace private style details with selectors and blanks.
- Keep style choices traceable: explain why the chosen route fits.
- Include rejected alternatives when they prevent style drift.
- Do not store confidential source material in `style-brief`.
