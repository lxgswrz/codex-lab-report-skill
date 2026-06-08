# Analysis Writing Requirements

## General Principle

The analysis section must follow the lab guide's report requirements. Do not write one generic paragraph when the guide lists multiple comparison tasks. Convert each requirement into a clear item or subsection.

## Recommended Structure

For each analysis item:

1. Start with a bold numbered title.
2. Put the explanation on the next line as a new paragraph.
3. State what the guide asks to compare or discuss.
4. Give measured result, theoretical result, and deviation.
5. Explain the physical reason for agreement or disagreement.

Example pattern:

```latex
\noindent\textbf{3. 赤道处交流激磁和直流激磁读数比较。}\par

指导书要求比较交流和直流激磁时赤道处高斯计读数，并与理论值比较。...
```

## What Counts as Detailed Analysis

Include:

- Trend description: increase/decrease/constant/nonlinear.
- Quantitative comparison: measured value, theory value, relative error.
- Physical mechanism: why the trend occurs.
- Model assumptions: ideal conductor, point probe, uniform field, no loss, etc.
- Measurement limitations: instrument response, alignment, positioning, reading uncertainty, waveform/phase.

Avoid:

- "基本符合理论" without values.
- "可能有误差" without source.
- Repeating table values without interpretation.
- Mixing two separate experiments into one undifferentiated conclusion.

## Combined Reports

If one PDF includes multiple experiments:

- Keep data processing clearly separated by experiment.
- Keep the analysis section separated by experiment.
- Each experiment's analysis should directly answer its own guide requirements.
- Use a final discussion only to summarize cross-experiment learning or general error sources.
