"""
Thesis build script using tectonic (bibtex backend — no separate biber needed).

Usage:
    uv run python build.py          # build PDF
    uv run python build.py --clean  # remove artefacts, then build
    uv run python build.py --open   # build and open PDF
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

THESIS_DIR = Path(__file__).parent
MAIN = "main"
ARTEFACTS = [".aux", ".bbl", ".bcf", ".blg", ".log", ".out",
             ".run.xml", ".toc", ".lof", ".lot"]


def run(cmd: list[str], label: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, cwd=THESIS_DIR)
    if result.returncode != 0:
        print(f"\n[ERROR] {label} failed (exit {result.returncode})")
        sys.exit(result.returncode)


def clean() -> None:
    for ext in ARTEFACTS:
        for f in THESIS_DIR.glob(f"**/*{ext}"):
            f.unlink()
    pdf = THESIS_DIR / f"{MAIN}.pdf"
    if pdf.exists():
        pdf.unlink()
    print("Cleaned build artefacts.")


def build() -> None:
    tectonic = shutil.which("tectonic")
    if not tectonic:
        print("[ERROR] tectonic not found. Install via: brew install tectonic")
        sys.exit(1)

    # tectonic handles bibtex passes automatically with --keep-intermediates
    run(
        [tectonic, "--keep-intermediates", f"{MAIN}.tex"],
        "tectonic — compiling thesis (auto bibtex passes)",
    )

    pdf = THESIS_DIR / f"{MAIN}.pdf"
    if pdf.exists():
        print(f"\n  Build successful → {pdf}")
    else:
        print("\n[ERROR] PDF not produced.")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the thesis PDF.")
    parser.add_argument("--clean", action="store_true",
                        help="Remove build artefacts before building")
    parser.add_argument("--open", action="store_true",
                        help="Open the PDF after a successful build")
    args = parser.parse_args()

    if args.clean:
        clean()

    build()

    if args.open:
        pdf = THESIS_DIR / f"{MAIN}.pdf"
        subprocess.run(["open", str(pdf)])


if __name__ == "__main__":
    main()
