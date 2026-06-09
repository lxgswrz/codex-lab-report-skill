# LaTeX and PDF Generation

## LaTeX Setup

Prefer a clean `ctexart` setup for Chinese-first printable reports:

```latex
\PassOptionsToPackage{table}{xcolor}
\documentclass[UTF8,fontset=windows,zihao=-4]{ctexart}
\usepackage[a4paper,left=2.35cm,right=2.0cm,top=2.0cm,bottom=2.0cm,bindingoffset=0.55cm]{geometry}
\usepackage{amsmath,amssymb,graphicx,booktabs,array,float,xcolor,caption,eso-pic}
```

If using `ctex` plus `xcolor`, prefer passing options before `\documentclass` to avoid package option clashes.

Keep headings left aligned:

```latex
\ctexset{
  section={format={\normalsize\bfseries\raggedright}},
  subsection={format={\normalsize\bfseries\raggedright}}
}
```

## Binding Line Snippet

Use precise character placement rather than a rotated text box:

```latex
\AddToShipoutPictureBG{%
  \AtPageLowerLeft{%
    \put(\LenToUnit{1.06cm},\LenToUnit{1.25cm}){%
      \color{black}\linethickness{0.45pt}%
      \multiput(0,0)(0,11){30}{\line(0,1){6}}%
    }%
    \put(\LenToUnit{1.06cm},\LenToUnit{17.25cm}){%
      \color{black}\linethickness{0.45pt}%
      \multiput(0,0)(0,11){30}{\line(0,1){6}}%
    }%
    \put(\LenToUnit{1.06cm},\LenToUnit{15.80cm}){\makebox(0,0)[c]{\zihao{-5}装}}%
    \put(\LenToUnit{1.06cm},\LenToUnit{15.05cm}){\makebox(0,0)[c]{\zihao{-5}订}}%
    \put(\LenToUnit{1.06cm},\LenToUnit{14.30cm}){\makebox(0,0)[c]{\zihao{-5}线}}%
  }%
}
```

## Compiler Strategy

Use the user's requested compiler when specified. Otherwise:

1. Prefer local Tectonic for simple report projects.
2. Fall back only when the project needs full-TeX features or Tectonic is genuinely blocked.

Typical local Tectonic command:

```powershell
& 'D:\tool\tectonic\tectonic.exe' 'main.tex'
```

## Windows And Tectonic Notes

Common issues and responses:

- `Option clash for package xcolor`:
  - Use `\PassOptionsToPackage{table}{xcolor}` before `\documentclass`, then load `\usepackage{xcolor}` once.
- Fontconfig warnings about Windows fonts:
  - These can be acceptable if the PDF renders correctly.
- Chinese or non-ASCII paths:
  - If Tectonic behaves strangely, try compiling in a temporary ASCII-only directory to distinguish content errors from path issues.
- Cache or font access failures:
  - Rerun with normal local filesystem access if the environment was sandboxed.
- Output success rule:
  - A `.pdf` must actually be created; a clean-looking `.tex` file alone is not enough.

## Visual QA

Render representative pages:

- Cover
- First body page
- A table-heavy page
- A formula or code-heavy page
- Analysis page
- Last page

Use `scripts/render_pdf_pages.py` if `pypdfium2` is available.

If page rendering is unavailable, do a fallback check by:

- confirming the PDF exists
- checking page count
- extracting text from key pages when possible
- explicitly noting the residual layout risk
