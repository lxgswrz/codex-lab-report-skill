import argparse
from pathlib import Path

import pypdfium2 as pdfium


def parse_pages(spec, total):
    if not spec:
        return list(range(total))
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            pages.extend(range(int(start) - 1, int(end)))
        else:
            pages.append(int(part) - 1)
    return [p for p in pages if 0 <= p < total]


def main():
    parser = argparse.ArgumentParser(description="Render selected PDF pages to PNG.")
    parser.add_argument("pdf")
    parser.add_argument("--pages", help="1-based pages, e.g. 1,3,5-7")
    parser.add_argument("--out", default="rendered_pages")
    parser.add_argument("--scale", type=float, default=1.5)
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(str(pdf_path))
    for idx in parse_pages(args.pages, len(doc)):
        bitmap = doc[idx].render(scale=args.scale)
        bitmap.to_pil().save(out / f"page_{idx + 1}.png")
    print(f"rendered {len(parse_pages(args.pages, len(doc)))} pages to {out}")


if __name__ == "__main__":
    main()
