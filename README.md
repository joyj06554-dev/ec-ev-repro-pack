# EC-EV Reproducibility Package

**Release:** v1.0  
**Study domain:** endothelial-cell / extracellular-vesicle bibliometric and altmetric analysis  
**Primary bibliographic source:** Web of Science Core Collection  
**Historical search date:** 10 June 2025  
**Final dataset:** 4,974 records

## Purpose

This repository preserves the evidence needed to audit and methodologically reproduce the study's literature retrieval, database refinement, record-level final inclusion, keyword extraction, and data-integrity checks.

## Verified search flow

| Set / stage | Operation | Historical count |
|---|---|---:|
| #1 | Endothelial-related topic query | 255,638 |
| #2 | Extracellular-vesicle-related topic query | 71,178 |
| #3 | `#1 AND #2` | 5,367 |
| #4 | Article OR Review; 2004–2025; English | 30,642,369 |
| #5 | `#3 AND #4` | 4,974 |
| Combined database refinement | `#3 − #5` | 393 removed |

The complete literal query strings are stored in `01_search/search_strategy_verbatim.txt` and are backed by the supplied Supplementary Table 2 image.

## Important provenance statement

The 393-record reduction from #3 to #5 was produced by a **single combined Web of Science refinement query**. It is therefore reported as an aggregate database refinement, not as a manual title/abstract or full-text screening step.

The original 5,367-record pre-refinement export was not retained. The identities of those 393 removed records and criterion-specific exclusion counts are consequently unavailable and are not reconstructed retrospectively.

## Public data strategy

The final source dataset comprised 10 WoS Full Record and Cited References plain-text exports. Bulk raw WoS records are not redistributed in this public package. Instead, the repository includes:

- exact search history and historical result counts;
- SHA-256 hashes and counts for the source export files;
- a minimized record-level public index for all 4,974 final records;
- DOI when available and a SHA-256 title fingerprint;
- record-level final-scope labels;
- a raw author-keyword frequency dictionary;
- validation and regeneration scripts;
- software/version and parameter metadata;
- integrity manifests.

## Repository structure

- `01_search/` — exact search strategy, historical counts, primary evidence.
- `02_data/` — minimized public record index, codebook, source-file manifest and raw-data access note.
- `03_selection/` — database-refinement log and exclusion-provenance statement.
- `04_scope_classification/` — explicit operational scope rules and record-level scope labels.
- `05_keyword_dictionary/` — raw author-keyword dictionary and status documentation.
- `06_analysis/` — validation/regeneration scripts and parameters.
- `07_outputs/` — validation and publication-year summaries.
- `08_integrity/` — SHA-256 manifests.
- `09_docs/` — manuscript-ready statements and GitHub/Zenodo upload guide.

## Quick validation

With authorized copies of the original WoS exports:

```bash
python 06_analysis/scripts/validate_wos_dataset.py /path/to/private_wos_exports
```

Expected headline checks:
- total records: 4,974;
- unique WoS UT identifiers: 4,974;
- Article-class records: 3,669;
- Review-class records: 1,305;
- English-language records: 4,974;
- DOI present: 4,923;
- duplicate DOI: 0;
- unique sources: 1,045.

## Known limitations

1. The pre-refinement 5,367-record export was not retained, so record-level provenance for the 393 database-refinement removals is unavailable.
2. The original study-specific synonym/thesaurus file was not supplied; the repository therefore preserves a raw keyword dictionary without inventing retrospective synonym merges.
3. GUI-analysis settings that were not preserved in the supplied materials are marked as not retained rather than reconstructed.
4. Database contents evolve, so rerunning the same query at a later date may not reproduce historical result counts exactly.

## Creator

- **Honglin Jiang** — ORCID: 0000-0001-6012-8071
- Affiliation: The Second Affiliated Hospital of Chongqing Medical University

## Licensing

- Original scripts in `06_analysis/scripts/`: **MIT License**.
- Original documentation and author-generated derived data tables: **CC BY 4.0**.
- Third-party database content, including Web of Science records, is excluded from these grants and remains subject to the relevant provider terms.

See `LICENSE`, `LICENSE-CODE`, and `LICENSE-DATA-DOCS`.

## Citation

Citation metadata are provided in `CITATION.cff`. The associated article DOI has not yet been assigned. A Zenodo version DOI will be added to the live repository metadata after archival.
