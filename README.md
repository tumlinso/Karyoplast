# Karyoplast

Karyoplast is an experimental, learned generative model of cellular functioning
and development. Its long-term objective is for one simulated founder cell to
produce a developing population through persistent internal dynamics, division,
differentiation, signaling, and interactions, potentially giving rise to spatial
and multicellular organization.

The ambition extends beyond plausible expression profiles or isolated state
predictions: it is to learn enough of the underlying cellular system to support
autonomous, sustained behavior. **This repository is a research foundation, not
an implemented cellular model.** No architecture, training system, dataset, or
biological capability has been established.

## The conceptual vocabulary

| Term | Computational meaning |
| --- | --- |
| Genome | One shared set of trainable numerical model parameters governing all virtual cells. |
| Chromosomes | A loose analogy for parameter groups or conditional components, possibly including experts. No literal chromosome structure is required. |
| Cell | A persistent execution of the shared model with its own state, history, environment, and interactions. |
| Differentiation | Distinct behaviors arising through state and experience under shared weights. |
| Division | A generative transition producing daughter instances with shared weights and potentially distinct inherited states. |
| Development | The evolution of a population of interacting executions under shared learned dynamics. |

This is a metaphor, not a nucleotide-based implementation specification. The
learned genome is expected to consist of floating-point weights; biological
states are initially expected to use vectors, tensors, latent states, and
structured numerical variables. A represented biological genome is a different
object from those learned parameters. Exact genomic sequence and learned
numerical representations can coexist; future Baseplane grounding remains open.
Cells are not MoE experts, and outputs need not be natural language.

## Research principles

- One shared trainable genome; many independent, persistent cell states.
- Differentiation through state rather than inherently separate fine-tuned weights.
- Ultimately learned division and population development, with explicit physical
  and biological constraints where justified.
- Eventually improve the common model using observations and trajectories of
  interacting cells, including branching lineages.
- Evaluate predictions, repeated rollouts, and perturbation responses against
  experimental evidence. Predictive agreement does not establish the true mechanism.

An initial experiment should test a small, scientifically meaningful component.
It need not simulate an embryo or solve comprehensive cellular modeling.

## Related projects

Karyoplast should build upon **Cellerator** for structured scientific computation
and **Baseplane** for sequence-grounded representations. **GlassHelix** informs
observability, inference, and mechanistic validation. **Cytoplast** is the
prospective distributed model execution/training substrate; **FrameShift** is
the prospective logical lifecycle and interaction layer. **CellShard** provides
relevant storage/delivery infrastructure, and **Device Scheduler** owns physical
resource allocation.

These packages remain independent. See the [source-backed ecosystem assessment](docs/ecosystem.md)
for inspected interfaces, current limitations, and prospective dependencies.
No neighboring package is a runtime dependency of this scaffold.

## Getting started

Python 3.10+ is required. The package has no runtime dependencies.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python -c "import karyoplast; print(karyoplast.__version__)"
python -m unittest discover -s tests -v
```

The source-only smoke check needs no installation or third-party test runner:

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

These checks validate packaging only. See [development guidance](docs/development.md)
for offline installation and evidence conventions.

## Where to develop the ideas

- [Documentation map](docs/README.md): scientific vision, representations,
  architectural alternatives, and training/evaluation questions.
- [Provisional roadmap](planning/roadmap.md): foundations through population development.
- [Open decisions](planning/open-questions.md): questions still requiring research.
- [Decision record](planning/decisions.md): bounded foundation choices and rationale.
- [Project Control](docs/project-control.md): workspace discovery, orientation,
  planning authority, and verification evidence.
- [Agent instructions](AGENTS.md): operational boundaries for future sessions.

`src/karyoplast/` is the minimal importable package; `tests/` checks the scaffold.
`docs/` holds evolving scientific/design material, and `planning/` holds
reviewable proposals and decisions. The roadmap is exploratory, not authorization
to begin implementation, training, GPU experiments, or kernel development.
