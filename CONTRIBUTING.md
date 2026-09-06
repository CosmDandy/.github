# Contributing

Thanks for taking the time. These repositories are maintained by one person, so
small, focused changes get merged fastest.

## Before you start

- Open a pull request early as a draft if the change is more than a few lines.
  It saves both of us from work that would not be merged.
- Bugs and ideas: issues are disabled on most repositories. Describe the problem
  in the pull request itself, or reach out through the contacts on
  [cosmdandy.dev](https://cosmdandy.dev).

## Development environment

Every repository ships a `.devcontainer/` and works out of the box with
[DevPod](https://devpod.sh), VS Code Dev Containers, or GitHub Codespaces.
Tooling versions live there; you should not need to install anything globally.

## Pull requests

- One logical change per pull request.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org):
  `feat:`, `fix:`, `docs:`, `chore:`, `ci:`, `refactor:`, `test:`.
- Code, comments, and commit messages are in English.
- Run the repository's checks before pushing — a `Makefile`, `pyproject.toml`,
  or the workflows in `.github/workflows/` show what CI will run.
- Never commit secrets. Encrypt with sops or reference a CI secret.

## Licensing

By contributing you agree that your changes are released under the license of
the repository you contribute to.
