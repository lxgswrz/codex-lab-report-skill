# LaTeX and PDF Generation

## LaTeX Setup

Prefer:

```latex
\documentclass[UTF8,fontset=windows,zihao=-4]{ctexart}
\usepackage[a4paper,left=2.35cm,right=2.0cm,top=2.0cm,bottom=2.0cm,bindingoffset=0.55cm]{geometry}
\usepackage{amsmath,amssymb,graphicx,booktabs,array,float,xcolor,caption,eso-pic}
```

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

## Compile

Use local Tectonic when available:

```powershell
& 'D:\tool\tectonic\tectonic.exe' 'main.tex'
```

If Tectonic fails because of cache/font sandbox restrictions, rerun with normal filesystem access. Fontconfig warnings about Windows fonts can be acceptable when the PDF renders correctly.

## Visual QA

Render representative pages:

- Cover.
- First body page.
- A table-heavy page.
- Analysis pages.
- Last page.

Use `scripts/render_pdf_pages.py` if `pypdfium2` is available.
