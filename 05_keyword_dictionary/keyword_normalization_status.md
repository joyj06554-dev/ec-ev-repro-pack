# Keyword-dictionary status

This release preserves the raw author-keyword dictionary extracted from the WoS `DE` field.

No original thesaurus/synonym-mapping file was supplied. Therefore this repository does **not** invent or retroactively attribute synonym merges, abbreviation expansion, singular/plural collapsing or term exclusions to the original study.

The raw dictionary is suitable for audit and for constructing a future, version-controlled thesaurus. Any new normalization layer should be stored as a separate file with explicit mappings (`raw_term -> standardized_term`), rationale, reviewer and version, and should not overwrite the raw dictionary.
