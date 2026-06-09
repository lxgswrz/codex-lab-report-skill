---
name: lab-report-pdf
description: Write, revise, format, compile, and visually verify polished Chinese-first experiment reports as LaTeX/PDF artifacts. Use when the user wants a printable lab report, references an existing PDF report/template/cover, asks for LaTeX or Tectonic, needs formulas/tables/figures laid out cleanly, or wants a stable PDF deliverable rather than a Word document.
---

# Lab Report PDF

Use this skill when the final deliverable should be a compiled experiment-report PDF with editable LaTeX source.

This skill is the default choice when any of the following is true:

- The user asks for LaTeX, PDF, Tectonic, XeLaTeX, or a compiled report.
- The user gives a reference PDF and wants the new report to resemble it.
- The report contains formulas, multiple tables, figures, screenshots, code blocks, or binding-line layout that should print reliably.
- The user wants a stable submission artifact rather than an editable Word document.

Do not use this skill as the primary workflow when the user explicitly wants an editable `.docx`; in that case prefer `doc` or `office-academic-skill`.

## Routing First

Decide the deliverable before reading nearby report files:

1. If the user explicitly wants Word or editable Office output, do not use this skill as the primary workflow.
2. If the user asks for LaTeX, PDF, a reference-PDF style, or a local lightweight compiler, use this skill and stay on the LaTeX/PDF path even if `.docx` files already exist.
3. If the user names a compiler such as Tectonic, treat that as a requirement unless it provably cannot work.
4. If the user does not specify a compiler, prefer local Tectonic first for simple projects and full TeX only when clearly needed.

## Core Workflow

1. Collect inputs:
   - Lab guide or experiment handout.
   - Measured data, screenshots, photos, code, plots, or tables.
   - Reference report, reference PDF, pre-report, or formatting sample if provided.
   - Metadata: course, experiment name, teacher, class, student name, student number, date, location if needed.

2. Determine the report shape:
   - If a reference PDF or cover is supplied, inspect it before drafting.
   - Decide whether the report needs a separate cover page, binding line, page numbers, appendix, code section, or multi-experiment structure.
   - If multiple experiments are included, keep a unified cover/front matter and separate each experiment's data and analysis clearly.

3. Extract the actual requirements:
   - Read the lab guide's report requirements, analysis tasks, discussion prompts, or scoring items.
   - Use those items as the analysis checklist.
   - Do not collapse multiple required comparisons into one vague paragraph.

4. Build the report in LaTeX:
   - Use a clean, printable Chinese-first structure unless the guide or reference overrides it.
   - Put data processing before result analysis.
   - Use LaTeX math for formulas and unit-aware notation.
   - Keep tables readable; split wide tables instead of shrinking them aggressively.
   - Use figure captions and consistent section hierarchy.

5. Compile and verify:
   - Compile the `.tex` file into a real `.pdf`.
   - Render or otherwise inspect representative pages.
   - Iterate until the PDF is visually clean and printable.

## Definition Of Done

The task is not complete until all required deliverables exist and pass a basic quality check:

- A `.tex` source exists.
- A compiled `.pdf` exists.
- The compiler actually succeeded in the current environment.
- The final response reports the output paths and the compiler used.
- If the user specified a compiler, the response states whether that exact compiler was used.

Do not stop after writing LaTeX source only. A missing or failed PDF build is an incomplete result.

## Standard Report Structure

Use this default structure unless the lab guide or reference format overrides it:

1. Cover
2. Experiment purpose and requirements
3. Experiment content and theory
4. Instruments and equipment
5. Data recording and processing
6. Results and analysis
7. Discussion, error analysis, or reflection
8. Optional appendix: code, screenshots, extra tables

## Writing Guidance

- Write in clear Chinese academic prose by default.
- Preserve English terms, commands, formulas, variable names, API names, and library names as needed.
- Tie each conclusion to data, formulas, plotted trends, screenshots, or theory.
- When theory exists, compare measured and theoretical values quantitatively.
- Explain error sources in terms of instruments, operation, assumptions, waveform quality, quantization, alignment, or physical mechanism.
- Avoid filler such as "matches theory" without values.

## Reference-Aware Layout

When a reference PDF or report is supplied:

- Inspect the cover structure first.
- Reproduce the style cues that matter for submission: cover layout, field order, title hierarchy, page numbering, binding line, section alignment, table tone, and spacing.
- Follow the reference's structure without copying unrelated content.
- If the reference conflicts with the lab guide, preserve the guide's content requirements and the reference's presentation style.

## Compiler Guidance

- Prefer local Tectonic when available and the project is simple enough.
- If the user explicitly asks for a lightweight local compiler, try Tectonic before other engines.
- Use the LaTeX compile workflow for actual builds; do not assume a `.tex` file is sufficient.
- If Tectonic fails, diagnose whether the failure is due to:
  - a LaTeX source problem,
  - path or encoding issues,
  - Windows cache or font access,
  - unsupported packages or full-TeX-only features.
- Only fall back to a full TeX workflow when the lightweight path is genuinely unsuitable or unusable.

## Visual QA

Inspect at least these pages when feasible:

- Cover
- First body page
- A page with dense tables
- A page with formulas or code
- Analysis or discussion page
- Final page

Look for:

- Wrong cover structure
- Missing binding line when needed
- Overflowing tables or code
- Broken Chinese text or missing fonts
- Stretched or clipped figures
- Awkward page breaks
- Tiny unreadable text

## When You Need Details

- Read `references/workflow.md` for the full workflow and report planning logic.
- Read `references/format.md` for cover, typography, tables, figures, and binding-line rules.
- Read `references/analysis.md` for analysis-writing requirements.
- Read `references/latex-pdf.md` for LaTeX setup, compilation strategy, Tectonic guidance, and PDF QA.

## Useful Script

- `scripts/render_pdf_pages.py` renders selected PDF pages to PNG for visual checking when `pypdfium2` is available.
