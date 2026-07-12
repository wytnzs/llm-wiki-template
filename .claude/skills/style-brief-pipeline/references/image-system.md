# Image System

Use this reference for illustrations, social-card visuals, chart beautification, and image prompts.

## Image Role

Images must do one of three jobs:

1. Explain an abstract idea.
2. Make a process or relationship visible.
3. Redraw data so the conclusion is easier to understand.

If an image does none of these, skip it.

## Material Explainer Style

Default look:

- off-white studio background
- black ink outlines
- refined gray or white material surfaces
- one vivid accent color
- soft contact shadows
- no stock-photo background
- no decorative blobs or bokeh
- no fake logos, watermarks, or UI chrome

Default accent: IKB blue `#002FA7`.

Use orange only for warning, migration, risk, or decision points. Use green for growth or optimization. Use red sparingly for failure or strict blocking states.

## Label Rules

- Use Simplified Chinese by default.
- Use 3-5 labels per image.
- Keep labels short, ideally 2-5 Chinese characters.
- Place labels near the object or arrow they explain.
- Do not put paragraph explanations inside the image.
- If labels are wrong or garbled, regenerate.

## Composition Patterns

| Pattern | Use When |
|---|---|
| Cycle | feedback loops, recurring work, iteration |
| Pipeline | step-by-step workflow or transformation |
| Hub-and-spoke | routing, orchestration, multi-branch systems |
| Before/after | upgrade, migration, cleanup, contrast |
| Layer stack | architecture, hierarchy, dependencies |
| Data-first scene | charts, metrics, benchmark, business data |

## Chart Beautification

For chart screenshots or data:

Keep:

- chart type
- title and conclusion
- exact values
- category order
- axis labels, ticks, ranges, and units
- error bars when present

Discard:

- screenshot colors
- source fonts
- weak layout
- shadows and background artifacts
- cramped spacing

Reject any beautiful chart with wrong data.

## Prompt Skeleton

Use this structure when producing an image prompt:

```text
Use case: [explainer / chart / social-card center image]
Asset type: [platform and ratio if known]
Primary request: [one concrete relationship or scene]
Chinese labels: [3-5 exact short labels]
Required accuracy: [data, order, names, units, if applicable]
Style: restrained material explainer, off-white background, black ink outlines, refined gray surfaces, one [accent] accent.
Composition: full subject visible, generous margins, labels away from edges, no crop.
Avoid: extra words, wrong labels, wrong data, logo, watermark, stock-photo background, dense legend, decorative blobs.
```

If exact dimensions are required, verify current platform requirements before writing them into the final prompt.
