# .github

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/CosmDandy/.github)
[![Edit in github.dev](https://img.shields.io/badge/edit-github.dev-1f6feb?logo=github)](https://github.dev/CosmDandy/.github)

Default community health files for all `CosmDandy` repositories.

GitHub falls back to the files here whenever a repository has no file of its own
(in its root, `.github/`, or `docs/`): `SECURITY.md`, `CONTRIBUTING.md`,
`PULL_REQUEST_TEMPLATE.md`, `ISSUE_TEMPLATE/`. A repository that needs a
different policy overrides it by adding the file locally.

## What else lives here

- `.github/release.yml` — the changelog categories every repository inherits for
  `gh release create --generate-notes`. Copy it into a repository that needs its
  own categories; release notes config is **not** inherited automatically.
- `social-preview/` — 1200×630 images for the Settings → Social preview field,
  which has no API and is set by hand.
