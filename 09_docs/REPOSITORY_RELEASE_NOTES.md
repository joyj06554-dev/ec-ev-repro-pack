# Repository release notes — v1.0

This release is the first public-release structure of the EC-EV reproducibility package.

Key decisions:
- The exact WoS #1–#5 strategy is treated as verified primary evidence.
- The 5,367 → 4,974 reduction is described as a combined database refinement, not manual screening.
- No record-level identities or criterion-specific reasons are assigned to the 393 removed records because the pre-refinement export was not retained.
- The public record index is data-minimized: complete titles and full WoS records are not redistributed.
- A SHA-256 title fingerprint is supplied for matching/integrity without reproducing title strings.
- Scope is operationally defined by membership in final WoS query #5.
- Raw author keywords are preserved without inventing a retrospective synonym thesaurus.
- Audit scripts are separated from any claim about the original software workflow.

Release metadata frozen for v1.0:
- Creator: Honglin Jiang (ORCID 0000-0001-6012-8071)
- Affiliation: The Second Affiliated Hospital of Chongqing Medical University
- Licensing: MIT (scripts) + CC BY 4.0 (documentation/derived data), excluding third-party database content
- Associated article DOI: not yet assigned
