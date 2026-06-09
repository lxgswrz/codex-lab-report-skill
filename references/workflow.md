# Experiment Report Workflow

## 1. Choose The Correct Deliverable

Start by deciding what the user actually wants:

- If the user explicitly wants Word editing, this skill should not be the main workflow.
- If the user wants a printable report, LaTeX, PDF, Tectonic, a reference-PDF style, or formula-heavy stable output, stay on the LaTeX/PDF path.
- If the user names a compiler, treat that as a real requirement.

Do this before reading nearby `.docx` files or reusing earlier Word-based report scripts.

## 2. Read The Sources

Locate:

- Experiment title and course name
- Experiment purpose
- Theory and formulas
- Instrument list
- Data-recording tables
- Exact report requirements, discussion items, or scoring items
- Any teacher or template requirements
- Any reference PDF or report whose visual structure should be mimicked

If the lab guide is a scanned PDF or text extraction is poor, render relevant pages and inspect them visually rather than trusting broken text extraction.

## 3. Plan The Report

Use this default structure unless the guide or reference format says otherwise:

1. Cover
2. Experiment purpose and requirements
3. Experiment content and theory
4. Instruments and equipment
5. Data recording and processing
6. Results and analysis
7. Discussion, error analysis, or reflection
8. Optional appendix

Before writing, decide:

- Separate cover page or inline front matter
- Binding line needed or not
- Single experiment or combined experiments
- Code section needed or not
- Figure-heavy, table-heavy, or theory-heavy layout emphasis

For combined reports, keep one unified cover/front matter and separate each experiment clearly in the data and analysis sections.

## 4. Process Data

For every measured quantity:

- State the raw measured value and unit
- Show the formula used for conversion
- Show at least one representative calculation when calculation matters
- Present final values with sensible significant digits
- Compare measured and theoretical values when theory is available

For plots:

- Label axes with quantity and unit
- Include measured and theoretical curves when relevant
- Refer to the plot explicitly in the analysis

## 5. Draft The Report

Write in Chinese academic style. Avoid generic statements without evidence. Keep formulas, variables, units, and commands in proper LaTeX form.

Use the lab guide requirements as the checklist for the analysis section. If the guide says "compare and discuss", include:

- what the data show
- whether it agrees with theory
- the quantitative deviation
- why the deviation is physically reasonable

If a reference PDF is provided, inspect its cover and page style first, then align the LaTeX structure to it.

## 6. Compile For Real

Do not stop at source generation.

- Produce a `.tex` file
- Compile it into a `.pdf`
- Report the actual compiler used
- If the requested compiler fails, explain why and whether you switched

## 7. Finalize

After compiling, inspect:

- Cover information and visual balance
- Tables, formulas, and code blocks
- Figures and captions
- Page breaks
- Binding line
- Font rendering
- No overlapping text or unreadably small content

The report is only complete when the PDF exists and the key pages look correct.
