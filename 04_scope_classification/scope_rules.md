# Operational scope-classification rules

The public package uses a transparent **query-defined operational scope**, rather than adding a retrospective thematic classification.

A record is labelled `EC_EV_FINAL_SCOPE` when it belongs to WoS search set #5:

- **SC01 — endothelial-related retrieval scope:** matches search set #1.
- **SC02 — extracellular-vesicle retrieval scope:** matches search set #2.
- **SC03 — intersection:** satisfies `#1 AND #2` (#3).
- **SC04 — document class:** Article or Review.
- **SC05 — publication period:** 2004–2025.
- **SC06 — language:** English.
- **FINAL:** `#3 AND #4` (#5).

All 4,974 records in `02_data/public_record_index.csv` carry `scope_label = EC_EV_FINAL_SCOPE`.

No additional manually assigned thematic subcategories are claimed in this release because no contemporaneous subcategory rulebook or record-level thematic labels were supplied. If such materials are recovered later, they should be added as a new repository version rather than inferred retrospectively.
