"""
Slides build script using tectonic (no separate bibtex/biber pass needed).

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

SLIDES_DIR = Path(__file__).parent
MAIN = "slide"
ARTEFACTS = [".aux", ".log", ".out", ".nav", ".snm", ".toc", ".vrb"]


def run(cmd: list[str], label: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, cwd=SLIDES_DIR)
    if result.returncode != 0:
        print(f"\n[ERROR] {label} failed (exit {result.returncode})")
        sys.exit(result.returncode)


def clean() -> None:
    for ext in ARTEFACTS:
        for f in SLIDES_DIR.glob(f"**/*{ext}"):
            f.unlink()
    pdf = SLIDES_DIR / f"{MAIN}.pdf"
    if pdf.exists():
        pdf.unlink()
    print("Cleaned build artefacts.")


def build() -> None:
    tectonic = shutil.which("tectonic")
    if not tectonic:
        print("[ERROR] tectonic not found. Install via: brew install tectonic")
        sys.exit(1)

    run(
        [tectonic, f"{MAIN}.tex"],
        "tectonic — compiling slides",
    )

    pdf = SLIDES_DIR / f"{MAIN}.pdf"
    if pdf.exists():
        print(f"\n  Build successful -> {pdf}")
    else:
        print("\n[ERROR] PDF not produced.")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the defense slides PDF.")
    parser.add_argument("--clean", action="store_true",
                        help="Remove build artefacts before building")
    parser.add_argument("--open", action="store_true",
                        help="Open the PDF after a successful build")
    args = parser.parse_args()

    if args.clean:
        clean()

    build()

    if args.open:
        pdf = SLIDES_DIR / f"{MAIN}.pdf"
        subprocess.run(["open", str(pdf)])


if __name__ == "__main__":
    main()
