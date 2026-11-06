---
name: safe-release-review
description: Review a repository change for private, oversized, generated or unlicensed content before an authorised release.
---

# Safe release review

Use before publishing a repository, package or other source bundle. This review does not grant permission to publish; follow the user's authorisation and repository ownership rules.

1. Inspect the exact staged diff and all files reachable from the release commit, including relevant history when publishing a repository.
2. Check for credentials, personal or customer data, restricted research material, machine paths, virtual environments, caches, databases, build output and unexpectedly large binaries.
3. Check third-party code and assets for licence and attribution requirements; do not add a blanket licence unless contributors have authority to grant it.
4. Run available secret scanning and inspect any findings. Record checks that could not be performed.
5. Report the release scope and unresolved risks. Publish only when specifically authorised.
