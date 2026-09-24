#!/usr/bin/env python3
"""Build a minimized public record index from WoS plain-text exports."""
from pathlib import Path
import collections, csv, hashlib, re, sys

def start_num(path):
    m = re.search(r"download_(\d+)_", path.name)
    return int(m.group(1)) if m else 10**9

def parse(path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    records, cur, last = [], None, None
    for line in text.splitlines():
        if line.startswith("PT "):
            if cur is not None:
                records.append(cur)
            cur = collections.defaultdict(list)
            cur["PT"].append(line[3:].strip())
            last = "PT"
        elif line.startswith("ER"):
            if cur is not None:
                records.append(cur)
                cur = None
            last = None
        elif cur is not None:
            if len(line) >= 3 and line[:2].strip() and line[2] == " ":
                last = line[:2]
                cur[last].append(line[3:].strip())
            elif line.startswith("   ") and last:
                val = line[3:].strip()
                if last in {"AU","AF","CR"}:
                    cur[last].append(val)
                elif cur[last]:
                    cur[last][-1] = (cur[last][-1] + " " + val).strip()
    if cur is not None:
        records.append(cur)
    return records

def first(r, k):
    return r.get(k, [""])[0] if r.get(k) else ""

if len(sys.argv) != 3:
    raise SystemExit("Usage: build_public_record_index.py <raw_wos_folder> <output_csv>")

raw_dir = Path(sys.argv[1])
out = Path(sys.argv[2])
records = []
for f in sorted(raw_dir.glob("*.txt"), key=start_num):
    records.extend(parse(f))

with out.open("w", newline="", encoding="utf-8-sig") as fh:
    fields = ["record_id","doi","title_sha256","publication_year","document_class",
              "language","scope_label","final_inclusion","provenance_status"]
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    for i, r in enumerate(records, 1):
        title = first(r, "TI").strip()
        dt = first(r, "DT")
        cls = "Article" if "Article" in dt else ("Review" if "Review" in dt else "")
        w.writerow({
            "record_id": f"EC_EV_{i:06d}",
            "doi": first(r, "DI").strip().lower(),
            "title_sha256": hashlib.sha256(title.encode("utf-8")).hexdigest() if title else "",
            "publication_year": first(r, "PY"),
            "document_class": cls,
            "language": first(r, "LA"),
            "scope_label": "EC_EV_FINAL_SCOPE",
            "final_inclusion": "include",
            "provenance_status": "verified_member_of_final_4974"
        })
print(f"Wrote {len(records)} records to {out}")
