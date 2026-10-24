# Foundation decision record

## KARYO-D001 — Numerical shared-genome interpretation

Status: established project intent, 2026-10-24.

Use genome/chromosome/cell as a conceptual vocabulary. Expect one shared set of
numerical trainable weights with distinct per-cell numerical state. Do not
encode neural parameters as nucleotide strings or assign separate weights as a
requirement for differentiation. Represented biological genomes remain distinct.

Rationale: the user's scientific intent concerns shared learned dynamics and
inheritance, not literal nucleotide execution. Exact sequence and numerical
representations may coexist through Baseplane. Reconsider concrete state and
sequence mechanisms as experiments provide evidence; the metaphor alone is
not such evidence.

## KARYO-D002 — Minimal independent Python scaffold

Status: adopted for initialization, 2026-10-24.

Use `src/karyoplast/`, setuptools, Python 3.10+, no runtime dependencies, and
standard-library smoke tests. Retain separate neighboring packages. Add no
model abstractions, adapter implementations, C++/CUDA build, or training stack.
No license has been selected.

Rationale: the initial deliverable is an understandable workspace where research
can constrain architecture. Alternatives such as a Torch-first framework or
native build add commitments before a consumer problem exists. Reconsider when
a bounded experiment demonstrates a concrete need.

## KARYO-D003 — Research proposals remain provisional

Status: adopted for initialization, 2026-10-24.

Keep scientific alternatives in `docs/`, unresolved questions and roadmap in
`planning/`, and source-backed inspection/validation records in `docs/evidence/`.
Project Control registration/discovery does not adopt the roadmap as active work.
No model architecture or dataset is selected.

Rationale: prediction, latent dynamics, and causal/mechanistic inference have
different evidence requirements. Prematurely freezing interfaces or activating
a comprehensive implementation would obscure unresolved scientific choices.
Reconsider planning granularity when the user adopts a bounded experiment.
