# Format Requirements

## Cover

When a pre-report/reference cover is supplied, mimic it. Otherwise use a clean Chinese lab-report cover:

- Large centered title: course name on one line, `实验报告` on the next.
- Middle field rows with underlines:
  - 实验名称
  - 课程名称
  - 指导教师
  - 班级
  - 姓名
  - 学号
- Bottom field: 实验日期

Keep cover text centered and visually balanced.

## Body Typography

- Use one consistent body font size.
- Keep table text the same size as body text unless the reference template clearly differs.
- Section and subsection titles should be left aligned unless the provided reference explicitly centers them.
- Do not use viewport-like scaling or tiny table fonts.
- Do not shrink wide tables with `\resizebox`; split them into multiple tables.

## Binding Line

For printable reports that need a binding line:

- Place it on the left side of body pages.
- Use a vertical dashed line.
- Put `装`, `订`, `线` in the center gap, each character separately aligned on the vertical line.
- Keep the line far enough left that it does not collide with body text.

## Tables

Tables should:

- Include units in headers.
- Use clear captions.
- Avoid too many columns.
- Split into multiple tables when needed:
  - raw measurements
  - converted values
  - theory/comparison/deviation

## Formulas

Use LaTeX math for all equations. For important calculations:

```latex
\[
L=\frac{U_L}{\omega I}
=\frac{20.2}{2\pi\times4940\times1}
=0.651\,\mathrm{mH}
\]
```

Variables and units should be upright where appropriate: `\mathrm{V}`, `\mathrm{cm}`, `\mathrm{Gs}`.

## Figures

Figures should:

- Use readable labels and legends.
- Include measured and theoretical values when comparing.
- Be referenced in the text.
- Not be stretched, blurry, or clipped.
