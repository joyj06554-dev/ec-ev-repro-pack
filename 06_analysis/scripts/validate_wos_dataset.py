#!/usr/bin/env python3
from pathlib import Path
import collections, re, sys

def start_num(path):
    m=re.search(r"download_(\d+)_",path.name)
    return int(m.group(1)) if m else 10**9

def parse(path):
    text=path.read_text(encoding="utf-8-sig",errors="replace")
    records=[]; cur=None; last=None
    for line in text.splitlines():
        if line.startswith("PT "):
            if cur is not None: records.append(cur)
            cur=collections.defaultdict(list); cur["PT"].append(line[3:].strip()); last="PT"
        elif line.startswith("ER"):
            if cur is not None: records.append(cur); cur=None
            last=None
        elif cur is not None:
            if len(line)>=3 and line[:2].strip() and line[2]==" ":
                last=line[:2]; cur[last].append(line[3:].strip())
            elif line.startswith("   ") and last:
                val=line[3:].strip()
                if last in {"AU","AF","CR"}: cur[last].append(val)
                elif cur[last]: cur[last][-1]=(cur[last][-1]+" "+val).strip()
    if cur is not None: records.append(cur)
    return records

def first(r,k): return r.get(k,[""])[0] if r.get(k) else ""

root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(".")
records=[]
for f in sorted(root.glob("*.txt"),key=start_num):
    rs=parse(f); print(f"{f.name}\t{len(rs)}"); records.extend(rs)

uts=[first(r,"UT") for r in records]
dois=[first(r,"DI").lower() for r in records if first(r,"DI")]
print("TOTAL",len(records))
print("UNIQUE_UT",len(set(uts)))
print("DOI_PRESENT",len(dois))
print("DUPLICATE_DOI",len(dois)-len(set(dois)))
print("ARTICLE_CLASS",sum("Article" in first(r,"DT") for r in records))
print("REVIEW_CLASS",sum("Review" in first(r,"DT") for r in records))
print("LANGUAGES",dict(collections.Counter(first(r,"LA") for r in records)))
print("UNIQUE_SOURCES",len({first(r,"SO") for r in records if first(r,"SO")}))
