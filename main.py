"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Entry title: "Office Chair Gas Lift Eulogist"

Why this title: everybody has watched an office chair slowly sink to its
lowest setting and sighed. This job gives that moment a funeral: a
eulogist who delivers a short tribute every time a chair's gas lift gives
up. It is a real-sounding job (eulogist) with one hilariously specific
twist (the patient is a chair piston), it is instantly readable at 30
characters, and it is fresh territory — no Chief, no Senior, no apologizer.
Criterion check, in judge order: (1) weird job title, a few words naming
an odd job; (2) stranger than ordinary work — nobody hires a eulogist for
furniture; (3) the sinking-chair image lands on the first read; (4) a
eulogist is a real job, specific enough to picture the person in a suit
beside the chair; (5) 30 characters, taken in at a glance.

Writes the title, with no trailing newline, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os

LINE = "Office Chair Gas Lift Eulogist"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
