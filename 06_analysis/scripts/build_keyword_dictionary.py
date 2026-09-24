#!/usr/bin/env python3
"""Extract a raw author-keyword frequency dictionary from WoS plain-text exports."""
from pathlib import Path
import collections, csv, re, sys

def start_num(path):
    m = re.search(r"download_(\d+)_", path.name)
    return int(m.group(1)) if m else 10**9

def parse_de(path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    terms = []
    current_de = None
    for line in text.splitlines():
        if line.startswith("DE "):
            current_de = line[3:].strip()
            terms.extend([x.strip() for x in current_de.split(";") if x.strip()])
        elif line.startswith("   ") and current_de is not None:
            cont = line[3:].strip()
            terms.extend([x.strip() for x in cont.split(";") if x.strip()])
        elif len(line) >= 3 and line[:2].strip() and line[2] == " " and not line.startswith("DE "):
            current_de = None
    return terms

if len(sys.argv) != 3:
    raise SystemExit("Usage: build_keyword_dictionary.py <raw_wos_folder> <output_csv>")

raw_dir = Path(sys.argv[1])
out = Path(sys.argv[2])
counter = collections.Counter()
for f in sorted(raw_dir.glob("*.txt"), key=start_num):
    counter.update(parse_de(f))

with out.open("w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["raw_author_keyword","frequency","dictionary_status"])
    for term, n in sorted(counter.items(), key=lambda x: (-x[1], x[0].lower())):
        w.writerow([term, n, "raw_WoS_DE_term_no_synonym_merge"])
print(f"Wrote {len(counter)} unique raw keyword terms to {out}")
