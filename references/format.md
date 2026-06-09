# Format Requirements

## Cover

When a reference cover or reference PDF is supplied, mimic its structure first. Otherwise use a clean Chinese lab-report cover with:

- a strong centered title block
- a clear experiment title
- course, teacher, class, name, student number, and date fields
- balanced vertical spacing

Typical field labels include:

- 实验名称
- 课程名称
- 指导教师
- 班级
- 姓名
- 学号
- 实验日期

Keep the cover visually centered and not crowded. If the reference uses a separate cover page, do the same.

## Body Typography

- Use one consistent body font size.
- Keep table text at or near body text size unless the reference clearly differs.
- Keep section and subsection titles left aligned unless the reference explicitly centers them.
- Avoid tiny fonts, compressed tables, and ornamental formatting.
- Do not shrink wide tables with `\resizebox`; split them into multiple tables or reorganize columns.

## Binding Line

For printable reports that need a binding line:

- Place it on the left side of body pages, not on the cover unless the template explicitly does so.
- Use a vertical dashed line.
- Put the three characters `装` `订` `线` separately along the line.
- Keep it far enough left that it never collides with text.

## Tables

Tables should:

- include units in headers
- use clear captions
- avoid excessive column count
- prefer logical splitting when a table becomes too wide

Common split patterns:

- raw measurements
- converted values
- theory/comparison/deviation

## Formulas

Use LaTeX math for all equations. For important calculations, show a readable multi-line derivation when useful:

```latex
\[
L=\frac{U_L}{\omega I}
=\frac{20.2}{2\pi\times4940\times1}
=0.651\,\mathrm{mH}
\]
```

Keep variables italicized and units upright where appropriate, such as `\mathrm{V}`, `\mathrm{cm}`, `\mathrm{Hz}`, `\mathrm{mH}`.

## Figures

Figures should:

- use readable labels and legends
- include measured and theoretical values when comparing
- be cited in the surrounding text
- not be stretched, blurry, clipped, or disproportionately scaled

## Code And Screenshots

If the experiment requires code, debugger screenshots, serial output, or waveform captures:

- keep them legible
- give them captions when they support the analysis
- avoid full-page screenshots unless detail genuinely requires it
- do not let screenshots replace explanation
