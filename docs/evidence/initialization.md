# Initialization evidence — 2026-10-24

Scope: repository/scientific foundation and Project Control setup only. No model,
training, data download, GPU work, substantive native code, or neighboring source
modifications were performed.

## Python package validation

Validated by the configured Luna implementer on Python 3.13.11 with setuptools
80.9.0. Python 3.10 is the declared minimum, not an independently tested version.

- `PYTHONPATH=src python -m unittest discover -s tests -v`: 1 test passed.
- A disposable environment was created with
  `python -m venv --system-site-packages /tmp/karyoplast-validation-venv`.
- Its Python ran `-m pip install --no-deps --no-build-isolation .`: installation
  and wheel construction succeeded without fetching dependencies.
- From `/tmp`, the installed import resolved to the validation environment's
  `site-packages/karyoplast/__init__.py`. Package version and
  `importlib.metadata.version('karyoplast')` both equaled `0.1.0`.
- Installed-package unittest discovery also passed 1 test.
- `pip wheel --no-deps --no-build-isolation --wheel-dir /tmp/karyoplast-wheel-check .`
  produced `karyoplast-0.1.0-py3-none-any.whl`.
- Compile and whitespace checks passed. Pytest and the `build` package were not
  available; neither was used. Smoke tests validate the scaffold, not biology.

## Project Control registration and activation

The installed supported CLI registered workspace/repository `karyoplast` with
display name `Karyoplast` at `/home/tumlinson/Karyoplast`; `workspace list`
confirmed it. The registry's sole repository is its authority repository alias.
This is separate from a Todo semantic authority or an adopted research plan.

At the user's request, `project-control.service` was restarted. The service
manager reported it active, with PID `2870906`, started at
`2026-10-24T17:00:11Z`. A fresh MCP HTTP connection to the running observer
resolved Karyoplast. Health, readiness, and version endpoints returned HTTP 200;
core readiness was `ready`, Project Control version `0.4.2`.

The optional central inference supervisor was unavailable in the readiness
response. Inference was not required for registration, metadata, source search,
or exact reads; no inference service was started for this setup.

The source-backed `research-foundation` orientation was previewed and applied
through the installed mutator's supported `amend_project` API. Metadata revision
advanced from 0 to 1. It records the objective, scaffold-only status, shared-weight
interpretation, navigation, next research direction, and unresolved decisions.
The README content hash is its source anchor. See the reviewable request,
preview, and apply receipts under [project-control/](project-control/).

## Discovery and authority boundaries

The repository's tracked Python, Markdown, and TOML files are supported discovery
inputs. An unborn Git branch initially limited worktree-aware source context;
the authorized foundation commit supplies its first valid HEAD. Exact observer
reads and fixed-string matches already resolved the new documentation before it.

After foundation commit `aecd26cc10e86aef55d7c90eef13080c57c4f5d5`, a fresh
connection verified:

| Check | Result | Receipt |
| --- | --- | --- |
| Standard overview | Authored orientation present; summary freshness `fresh`; `README.md`, `AGENTS.md`, `pyproject.toml` discovered as entry points. | [overview](project-control/overview.json) |
| Numerical representation search | `predominantly floating-point` resolved to `docs/representations.md`, line 7, through the private lexical index and live fallback. | [representation search](project-control/representation-search.json) |
| Open research question search | `minimal useful representation` resolved to `planning/open-questions.md`, line 7, through worktree-aware discovery. | [question search](project-control/questions-search.json) |
| Python source search | `Karyoplast research package` resolved to `src/karyoplast/__init__.py`; source commit and working-tree freshness were returned. | [package search](project-control/package-search.json) |
| Exact document excerpt | Representation foundations lines 1–23 returned `ok`, with a content hash. | [document read](project-control/read.json) |
| Exact source/config reads | Package source and `pyproject.toml` returned `ok`, with content hashes. | [package reads](project-control/package-read.json) |

Assertions checked fresh orientation, all three entry points, expected source
paths, valid source-commit identity without a worktree-unavailable error, and
successful exact reads. These receipts capture in-progress working-tree state
while verification records were being written. The source hashes identify the
actual inspected files. Compact overview can require a continuation; use
`detail="standard"` for useful orientation in one response.

The existing chat's startup-bound stdio connection continued reporting
`project_not_permitted` after service restart; verification uses a fresh
connection to the restarted service. Reconnecting an older stdio frontend loads
the new registry without changing project permissions by hand.

No Todo authority, executable research plan, or task completion assertions were
created. Overview may therefore report `todo_workflow_semantic_unavailable` and
semantic revision omissions while still returning authored orientation and
source discovery. These limits must not be reported as completed workflow setup.

Final documentation checks found no broken local Markdown links; staged
whitespace checks passed. Registration metadata and live readiness results are
retained in [registration](project-control/registration.json) and
[service readiness](project-control/service-readiness.json).

## Neighboring interfaces

[The ecosystem assessment](../ecosystem.md) distinguishes existing source
surfaces from prospective scientific, execution, and training capabilities.
[The inspection manifest](ecosystem-inspection.json) records seven repositories
and 24 file hashes, including dirty-working-tree qualifications. No external
integration was built or run. General differentiable cellular dynamics,
Cytoplast execution/training, Baseplane learned genomic conditioning, and
Karyoplast numerical lifecycle adapters remain unqualified or prospective.
