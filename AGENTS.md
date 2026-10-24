# Working in Karyoplast

Read `README.md`, `docs/README.md`, and the relevant design notes before changing
scientific assumptions. This is a scientific research workspace with a package
scaffold, not an established biological model.

## Scientific and architectural boundaries

- Biological and mathematical correctness take precedence over convenient
  software assumptions. Label goals, hypotheses, proposals, implementations,
  and validated results explicitly; never silently promote one into another.
- Genome/chromosome/cell are architectural metaphors. Expect shared numerical,
  predominantly floating-point weights and numerical biological-state
  representations. Do not encode weights as DNA or require literal chromosomes.
- Distinguish learned parameters, per-cell state/history, represented biological
  genomes, and observed measurements. Baseplane sequence grounding is open;
  exact sequence and learned embeddings are compatible directions.
- Cells execute one shared model with distinct persistent state. Differentiation
  should not inherently require separate weights. Experts are model components,
  not cells. Inputs and outputs need not be text or language-model tokens.
- Prefer existing Cellerator and Baseplane capabilities over duplicating their
  infrastructure. Inspect current source, contracts, and evidence before an
  integration; missing scientific/autograd operators remain prospective.
- Keep package boundaries independent and architecture modular. Cytoplast owns
  prospective numerical execution/training, FrameShift logical lifecycle and
  interaction, and Device Scheduler physical resource allocation. No adapter
  contract is selected yet. See `docs/ecosystem.md` before proposing one.
- Distinguish observable prediction, learned latent dynamics, and mechanistic or
  causal inference. State uncertainty, latent/unobserved dynamics, and evidence
  limits. Good rollout predictions alone do not identify the true mechanism.
- Prefer small, testable experiments. Add complexity, dependencies, C++ or CUDA
  only for a concrete experimental need. The roadmap does not authorize execution.

## Repository practice

- Python source belongs in `src/karyoplast/`; tests in `tests/`. There are no
  runtime dependencies. Use `PYTHONPATH=src python3 -m unittest discover -s tests -v`
  for scaffold checks; test installed behavior when packaging changes.
- Put scientific explanations and alternatives in `docs/`. Record consequential
  choices, rationale, evidence, and reconsideration conditions in
  `planning/decisions.md`; keep unresolved choices in `planning/open-questions.md`.
- Record experiment inputs, units, time conventions, dataset/provenance and
  split identities, source revision, precision, seed, commands, and limitations.
  Keep large data/checkpoints local; retain small reviewable manifests and results.
- Preserve unknown edits, source packages, histories, and authority state.
  Do not modify neighboring projects without explicit authorization.
- Use Project Control project/repository selector `karyoplast` for useful
  context. Read `docs/project-control.md` for registration and connection limits.
  Planning files are proposals, not live task state. If Todo is established,
  use supported workflow APIs; never hand-edit SQLite or generated projections.
- Use configured Codex Luna specialists for substantial delegated engineering;
  give coherent ownership and validation responsibility. Do not use Project
  Control `delegate_task` or `local-coding-worker` for engineering. Root retains
  integration and final acceptance. Follow the session's model-allocation policy.
- Future GPU kernel work must consult `/home/tumlinson/kda/docs/agent-entry.md`
  and relevant pinned skills, and obey active resource admission controls.
  Initialization does not authorize model training or GPU work.
