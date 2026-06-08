---
name: lab-report-pdf
description: Write, revise, format, and generate polished Chinese experiment reports as LaTeX/PDF artifacts. Use when the user provides a lab guide, measured data, screenshots, a pre-lab/report template, or asks to quickly produce another 实验报告 with consistent cover, sections, tables, formulas, analysis, discussion, binding line, and visual PDF checks.
---

# Lab Report PDF

## Core Workflow

Use this skill to turn a lab guide plus measured data into a complete Chinese experiment report. Prefer LaTeX/PDF when the user asks for stable printing, formulas, or binding-line layout; use DOCX only when the user explicitly wants Word.

1. Collect inputs:
   - Lab guide or experiment handout.
   - User's measured data, photos, screenshots, or tables.
   - Reference report/pre-report format, if provided.
   - Student/course metadata: course, experiment name, teacher, class, name, student number, date.

2. Extract report requirements:
   - Read the lab guide's "实验报告要求" or equivalent section.
   - Treat those requirements as the analysis outline.
   - If multiple experiments are combined, analyze each experiment separately.

3. Build the report:
   - Use the standard section order unless the guide/template overrides it.
   - Put raw data and calculations before the analysis.
   - Use LaTeX formulas for all equations.
   - Keep tables readable; split wide tables instead of shrinking font size.

4. Write analysis:
   - Tie every conclusion to a measured value, plotted trend, formula, or theory comparison.
   - Discuss both trend agreement and quantitative deviation.
   - Explain error sources in terms of instruments, operation, model assumptions, and physical mechanism.

5. Generate and verify:
   - Compile to PDF.
   - Render key pages to PNG and visually inspect cover, tables, equations, figures, binding line, and page breaks.
   - Iterate until the PDF is printable and visually clean.

## When You Need Details

- Read `references/workflow.md` for a full step-by-step report-writing process.
- Read `references/format.md` for cover, section, table, formula, figure, and binding-line requirements.
- Read `references/analysis.md` for how to write detailed analysis and discussion sections.
- Read `references/latex-pdf.md` for LaTeX/PDF generation and visual QA.

## Useful Script

- `scripts/render_pdf_pages.py` renders selected PDF pages to PNG for visual checking when `pypdfium2` is available.
