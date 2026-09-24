# Raw bibliographic data access

The source dataset consists of 10 Web of Science Core Collection plain-text exports ("Full Record and Cited References") containing the final 4,974 records.

The bulk raw WoS exports are **not included in this public release package**. Their filenames, record counts, file sizes and SHA-256 hashes are preserved in `source_file_manifest.csv`.

The public record index is deliberately minimized. It provides a stable package record ID, DOI when available, a SHA-256 title fingerprint, year, document class, language and final-scope label without reproducing the complete WoS record metadata.

Researchers with lawful access to Web of Science can re-run the archived query and use the supplied scripts and hashes to compare an authorized export against the archived dataset. Because bibliographic databases change over time, a later re-run may not reproduce the historical result counts exactly.

The pre-refinement 5,367-record export was not retained. Consequently, the identities of the 393 records removed by the combined database refinement are not available at record level.
