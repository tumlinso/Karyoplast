# Project Control workspace

## Identity and useful entry points

- Workspace/project selector: `karyoplast`
- Repository selector and authority repository alias: `karyoplast`
- Display name: `Karyoplast`
- Registered root: `/home/tumlinson/Karyoplast`
- Git origin: `https://github.com/tumlinso/Karyoplast.git`

The supported registration command is:

```sh
project-control workspace add karyoplast karyoplast /home/tumlinson/Karyoplast --display-name Karyoplast
project-control workspace list
```

The user authorized restarting `project-control.service` to load the
registration. A previously connected stdio frontend may still need reconnecting
because its project allowlist was bound at startup. Do not confuse a stale
connection's `project_not_permitted` with a missing registry entry.

Source discovery uses the registered Git repository and supported text formats.
Tracked `.py`, `.md`, and `.toml` files cover `src/`, `tests/`, documentation,
and planning. No C++ semantic index or custom provider is needed for this
foundation. Project Control's security deny patterns and `.gitignore` serve
different purposes; local datasets, checkpoints, and secrets must stay out of
tracked discovery material.

## Context a future session should retrieve

Use `overview(project="karyoplast", detail="standard")` for scope/status and
repository entry points. Compact responses may provide a packet continuation
when the source-backed orientation exceeds their response budget.
Use `search` for discovery and exact supported typed lookups. An observer can
use `read` for exact paths; a coding agent can read source directly with Git/rg.

| Need | Source |
| --- | --- |
| Purpose, numerical genome metaphor, current limits | `README.md` |
| Operational boundaries | `AGENTS.md` |
| Scientific vision and latent/unobserved dynamics | `docs/scientific-vision.md` |
| Parameters versus biological state/sequence | `docs/representations.md` |
| Candidate architectures and scientific operators | `docs/architecture.md` |
| Prediction versus mechanism and evaluation | `docs/training-evaluation.md` |
| Source-backed integration assessment and gaps | `docs/ecosystem.md` and `docs/evidence/ecosystem-inspection.json` |
| Next research directions and unresolved choices | `planning/roadmap.md`, `planning/open-questions.md`, `planning/decisions.md` |

Project Control supports authored orientation via the mutator's `amend_project`
operation. Orientation must summarize these sources with content-hash anchors,
be previewed before applying, and use the current metadata revision and operation
identity. It is metadata, not a Todo plan or evidence that a model works. When
anchored source changes, refresh the declaration through that supported route
rather than hand-editing host state.

## Planning and authority

This initialization does not adopt the provisional roadmap as executable work
or create a research Todo plan. Registering an authority repository alias does
not initialize a Todo semantic authority. Missing Todo state is an explicit
boundary, not permission to invent task completion records.

If a plan is later adopted, use the installed Project Control workflow/plan
tools and current schemas. Begin with the supported `next_task` front door for
registered authoritative work. Never edit authority databases or generated
Markdown/JSON projections directly. Keep scientific proposals and their
evidence in versioned repository files.

## Verification record

The [initialization receipt](evidence/initialization.md) records registration,
service activation, actual context retrieval, package validation, and any
remaining connection or authority limits. Source inspection alone does not
establish live service readiness; verify through a fresh service connection.
