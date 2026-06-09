# Analysis Writing Requirements

## General Principle

The analysis section must follow the lab guide's actual requirements. Do not compress multiple required comparisons into one generic paragraph. Convert each requirement into a distinct item, paragraph, or subsection.

## Recommended Structure

For each analysis item:

1. State what is being compared or discussed.
2. Give the measured result.
3. Give the theoretical, expected, or reference result when available.
4. Quantify the deviation or contrast.
5. Explain the physical or engineering reason.

Example pattern:

```latex
\noindent\textbf{3. 主频分量与理论值比较}\par

根据频谱结果，第 4 个频点的实测幅值为 $0.5298\,\mathrm{V}$，理论值约为
$0.5000\,\mathrm{V}$，相对误差约为 $5.96\%$。该误差主要来自信号源幅值设定、
ADC 参考电压偏差以及量化误差。
```

## What Counts As Detailed Analysis

Include:

- trend description: increase, decrease, constant, nonlinear, saturation, oscillation, leakage, or concentration of energy
- quantitative comparison: measured value, theory/reference value, absolute or relative error
- physical mechanism: why the trend occurs
- model assumptions: ideal conductor, ideal sampling, no loss, uniform field, linear region, etc.
- measurement limitations: instrument response, alignment, positioning, reading uncertainty, waveform quality, quantization, trigger stability

Avoid:

- "matches theory" without values
- "there may be error" without naming a source
- repeating table values without interpretation
- mixing separate experiments into one undifferentiated conclusion

## Combined Reports

If one PDF includes multiple experiments:

- keep data processing separated by experiment
- keep the analysis separated by experiment
- make each experiment answer its own guide requirements directly
- use a final overall discussion only for shared lessons or common error sources
