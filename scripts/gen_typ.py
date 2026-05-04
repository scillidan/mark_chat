# Authors: GLM-4.5🧙‍, scillidan🤡

import sys
import argparse
from pathlib import Path


def generate_typ(filename, fonts):
    typs_dir = Path("typs")
    typs_dir.mkdir(exist_ok=True)

    md_path = Path(f"{filename}.md")

    if not md_path.exists():
        print(f"Error: Markdown file not found for {filename}")
        sys.exit(1)

    font_str = ", ".join(f'"{f}"' for f in fonts)
    content = f"""#import "@preview/cmarker:0.1.8"

#set page(paper: "a6", margin: 5%)
#set text(font: ({font_str}), size: 8pt)
#set par(justify: true)

#cmarker.render(read("../{md_path.name}"))"""

    typ_path = typs_dir / f"{filename}.typ"
    typ_path.write_text(content, encoding="utf-8")
    print(f"Created: {typ_path}")
    return typ_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Typst file from Markdown")
    parser.add_argument("filename", help="Markdown filename (without .md extension)")
    parser.add_argument(
        "--font",
        action="append",
        dest="fonts",
        help="Font name (can be specified multiple times)",
    )
    args = parser.parse_args()

    fonts = args.fonts if args.fonts else ["MonaspiceNe NFM", "Sarasa Mono SC"]
    generate_typ(args.filename, fonts)
