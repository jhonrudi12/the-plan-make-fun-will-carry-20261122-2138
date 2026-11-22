"""Write the competition entry text to /output/entry.txt."""

import os

ENTRY = (
    "Day 1: list $150 Fiverr gig: verified 500-lead lists for dentists. "
    "Scrape directories, verify emails in code, deliver CSV in 24h. "
    "Spend $15 promoting it; send 50 agencies a free 20-lead sample. "
    "Edge: 24/7 programmatic verification, humans take days. "
    "Likely 3-5 sales: $450-750."
)


def main() -> None:
    # The gate counts 1-280 characters and rejects whitespace-only text,
    # so strip trailing whitespace before writing to keep the entry exact.
    text = ENTRY.rstrip()
    assert text, "entry text must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
