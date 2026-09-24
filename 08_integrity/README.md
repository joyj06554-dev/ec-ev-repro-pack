# Integrity manifests

`file_manifest.csv` and `file_manifest_sha256.txt` contain SHA-256 hashes for repository files other than the two manifest files themselves. The manifests intentionally exclude themselves to avoid recursive self-hashing.

`source_assets_sha256.csv` records hashes for the supplied source archive and primary image evidence used to assemble this release.
