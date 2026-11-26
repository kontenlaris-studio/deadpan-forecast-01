#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

One line: a deadpan weather forecast for Blorthaven, a city that
does not exist on Tuesdays, read flat as if it were routine.

The comedy is the absence of reaction: the forecaster treats the
city's Tuesday absence as a scheduling note ("plan accordingly"),
never as a surprise. 14 degrees and 4pm ground it in real
broadcast detail; the final clause carries the joke.
"""
import os

ENTRY = (
    "In Blorthaven, expect 14 degrees and light rain from 4pm, "
    "though the city will not be there on Tuesdays, "
    "so plan accordingly."
)


def main():
    assert len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, cap is 160"
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
