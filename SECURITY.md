# Security Policy

## Supported versions

Only the default branch and the latest release of each repository receive fixes.

## Reporting a vulnerability

Please do not open a public issue or pull request for security problems.

Use GitHub's private vulnerability reporting instead: open the **Security** tab
of the affected repository and click **Report a vulnerability**. The report is
visible only to the maintainer.

Include what you found, how to reproduce it, and the impact you expect. You will
get an acknowledgement within 7 days and a fix or a decision within 30 days.
Credit is given in the advisory unless you ask otherwise.

## Scope

Most repositories here are personal infrastructure, tooling, and self-hosted
services. Secrets are never committed in plain text: `*.sops.yaml` files are
encrypted with [sops](https://github.com/getsops/sops) and are safe to be public.
A decryptable secret in any repository is a vulnerability — report it.
