"""Publish the day-one money plan to /output/entry.txt.

The plan itself is a single paragraph the judge reads; this script only
assembles it from its sentences, checks the gate rules (1-280 characters,
not blank), and writes it out.
"""

import os

MIN_CHARS = 1
MAX_CHARS = 280
TARGET_DIR = "/output"
TARGET_NAME = "entry.txt"

PLAN_SENTENCES = [
    "Day 1: list $150 Fiverr gig: verified 500-lead lists for dentists.",
    "Scrape directories, verify emails in code, deliver CSV in 24h.",
    "Spend $15 promoting it; send 50 agencies a free 20-lead sample.",
    "Edge: 24/7 programmatic verification, humans take days.",
    "Likely 3-5 sales: $450-750.",
]


def assemble(sentences):
    """Join the plan sentences into the exact paragraph to publish."""
    return " ".join(sentences)


def check_paragraph(paragraph):
    """Raise unless the paragraph passes the competition gate rules."""
    size = len(paragraph)
    if size < MIN_CHARS or size > MAX_CHARS:
        raise ValueError(f"plan must be {MIN_CHARS}-{MAX_CHARS} chars, got {size}")
    if not paragraph.strip():
        raise ValueError("plan must not be only whitespace")
    if paragraph != paragraph.strip():
        raise ValueError("plan must not start or end with whitespace")


def publish(paragraph):
    """Write the checked paragraph to the output file."""
    os.makedirs(TARGET_DIR, exist_ok=True)
    path = os.path.join(TARGET_DIR, TARGET_NAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(paragraph)
    return path


def run():
    paragraph = assemble(PLAN_SENTENCES)
    check_paragraph(paragraph)
    publish(paragraph)


if __name__ == "__main__":
    run()
