# Ecosystem assessment

Direct documentation and source inspection on 2026-10-24 established the
following boundaries. This is an interface reconnaissance, not a build,
installation, compatibility, performance, or biological qualification. Neighboring
working trees include uncommitted material; exact inspected file hashes and
checkout identities are retained in [the inspection manifest](evidence/ecosystem-inspection.json).
Recheck decisive interfaces before use.

## Existing source surfaces and prospective uses

| Project | Verified source/documentation | Possible Karyoplast use and limits |
| --- | --- | --- |
| **Cellerator** | `python/cellerator/__init__.py` exposes typed declarations, `prepare_product2`, `product2_forward`, `product2_jvp`, `product2_vjp`, and capability-checked `prepare_mechanism`. `python/cellerator/torch/product2.py` provides a CPU FP32 first-order autograd adapter. | Prefer its structured state/relations and scientific operators over a duplicate numerical runtime. A specific derivative-capable operator exists; this does not establish a general differentiable cellular dynamical system or integrator. |
| **Baseplane** | `CMakeLists.txt` defines `Baseplane::seq`; `include/Baseplane/dna2.hh` includes compact sequence views, validity, scans, predicates, and events. README describes exact sequence plus learned hierarchical floating-point representations as the research direction. | Sequence meaning, provenance, and eventual genomic conditioning belong here. Existing exact-sequence interfaces do not establish a trained whole-genome encoder or Karyoplast Python adapter. |
| **GlassHelix** | `include/GlassHelix/core/observation.hh` distinguishes individual observations from population snapshots, destructive sampling, time units, and supplied candidate alternatives. README describes inference over competing dynamical explanations. | Inform observation semantics, observability, identifiability, perturbation analysis, and mechanistic claims. These contracts do not identify mechanisms automatically. |
| **Cytoplast** | `python/cytoplast/__init__.py` and `src/cytoplast.cpp` expose version metadata. `docs/interfaces.md` explicitly labels execution/backend/training contracts conceptual. | Intended distributed, virtualized conditional-model execution and eventual shared training. No execution engine, distributed backend, or training API is delivered by the inspected scaffold. |
| **FrameShift** | `src/frameshift/client.py` has `FrameShiftClient.spawn`, `send`, `inspect`, result/event access, cancellation, and handoff lifecycle methods. Backend docs describe `offers`, `admit`, `generate`, `release`; typed nontext CPU fixtures exist. | Logical identity, persistence, interaction, communication, delegation, suspension/resumption. Agent-frame and integer-token fixtures do not qualify arbitrary numerical tensors, differentiable state, biological time, division, or Cytoplast interoperability. |
| **CellShard** | `include/CellShard/access/adapter.cuh` defines archive descriptors, payload/selection views, and adapter capability flags. README describes storage, partitions, CSPACK delivery, and explicit neutral device/stream bindings. | Reuse data/storage/delivery infrastructure where a consumer requires it. It does not own the biological model, training semantics, or a general distributed model execution engine. |
| **Device Scheduler** | `packages/device-scheduler-mcp/src/device_scheduler_mcp/client.py` exposes `DeviceSchedulerClient.request_lease` through `leases.request`; `docs/using-v1.md` documents lifecycle usage. | Physical allocation and resource leases remain external to model execution. No resource request or live GPU qualification was performed here. |

Source entry points and guides:

- [Cellerator Python bindings](https://github.com/tumlinso/Cellerator/blob/main/docs/development/python-bindings.md)
- [Baseplane build/use guide](https://github.com/tumlinso/Baseplane/blob/main/docs/development/start.md)
- [GlassHelix scientific overview](https://github.com/tumlinso/GlassHelix/blob/main/README.md)
- [Cytoplast conceptual interfaces](https://github.com/tumlinso/Cytoplast/blob/main/docs/interfaces.md)
- [FrameShift backend guide](https://github.com/tumlinso/FrameShift/blob/main/docs/backends.md)
- [CellShard boundaries](https://github.com/tumlinso/CellShard/blob/main/README.md)
- [Device Scheduler usage](https://github.com/tumlinso/device-scheduler/blob/main/docs/using-v1.md)

These navigation links may evolve independently of the dated local inspection.
The manifest identifies the exact bytes inspected, including working-tree
material that may differ from the linked upstream revision.

## Important Cellerator distinctions

The inspected binding guide separates core Python, optional Torch, CUDA
mechanisms, and resident CUDA operations. Native availability is build-dependent.
The Product2 Torch adapter uses first-order input/coefficient gradients and
marks backward once-differentiable; its JVP returns detached results. The
resident `cellerator.torch.cuda` operations are forward-only and reject tensors
requiring gradients. Do not infer that every operation participates in autograd.

The separate `CelleraTorch/` workspace is documented as design-only, with
implementation on hold and outside component/build/package registration. Its
presence is not an available operator implementation.

Karyoplast may need differentiable dynamical-system integration, more biological
operators, constraints, and suitable gradient pathways. Their general forms and
availability remain prospective; inspect Cellerator before deciding whether to
reuse, extend through an authorized upstream change, or prototype a narrowly
scoped consumer operation. No neighboring repository was modified here.

## Boundaries to preserve

Karyoplast defines the scientific model and its experimental questions;
Cellerator owns reusable structured numerical computation; Baseplane owns
sequence grounding. GlassHelix addresses what the data support about hidden
dynamics and mechanism. Cytoplast and FrameShift have distinct numerical
execution and logical lifecycle roles. CellShard storage/delivery and Device
Scheduler physical admission must not become duplicate model runtimes.

There are no cross-project imports, gitlinks, path dependencies, or adapter
implementations in this scaffold. Actual dtype/device contracts, ownership,
time/causality, state snapshots, genome revisions, gradient/optimizer semantics,
and lifecycle interfaces remain [open decisions](../planning/open-questions.md).
