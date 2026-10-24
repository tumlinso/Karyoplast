# Architectural exploration

**Status: alternatives for investigation.** No network, execution protocol,
cell-state schema, or integration adapter has been selected or implemented.

## Candidate modeling mechanisms

| Candidate | Motivation to investigate | Questions a bounded experiment must answer |
| --- | --- | --- |
| Conditional computation / MoE | Shared parameters with selective functionality across differing cell states | What routes computation, which experts specialize usefully, how are capacity and routing trained, and does specialization remain stable during rollout? |
| Transformer/context mechanisms | History-dependent transitions and interactions | What is a biological token/event, how is time represented, and can context and memory remain bounded through division? |
| Recurrent or state-space mechanisms | Persistent compact state and repeated evolution | Does the state retain necessary history, remain stable, and expose useful observation or perturbation responses? |
| Structured learned dynamics | Combine neural transformations with explicit state and constraints | Which variables, conservation relations, and interactions should be supplied versus learned? |
| Hybrid numerical models | Combine learned terms with Cellerator scientific operators or numerical integration | Which operator and derivative contracts exist, and what error, stability, and stiffness properties are required? |

MoE is a leading direction, not a requirement to adapt a conventional language
model. Natural-language tokens, next-token loss, attention structure, and
existing expert dimensions have no automatic biological justification. A
conditional expert is a model component, not a cell type or independent cell.

## Shared execution and persistence

Every cell should reference one logical parameter set while owning distinct
state, history, environmental inputs, and interactions. A future implementation
must establish state ownership, lineage identity, random-state handling,
checkpoint/replay semantics, and behavior when training publishes new weights.
Shared weights do not imply shared mutable cell state.

Division is a learned generative transition in the long-term vision. Possible
approaches include a joint daughter-state distribution, inherited state with
learned asymmetric allocation, or hybrid continuous dynamics and discrete
events. None is adopted. Any approach must specify what is conserved, how
lineages are represented, and what evidence constrains inheritance.

An environment may be an explicit field, spatial neighborhood, interaction
graph, learned context, or hybrid. Signal propagation, asynchronous versus
synchronous updates, physical time, spatial organization, and population-level
feedback remain open. Simulation bookkeeping alone must not be presented as
learned autonomous behavior.

## Scientific operations and gradients

Build on Cellerator rather than duplicate its structured numerical substrate.
Its inspected Python surfaces include a bounded Product2 forward/JVP/VJP path
and optional Torch adapters. This is evidence of specific derivative operations,
not a general differentiable cellular simulator. Resident CUDA operations have
distinct forward-only constraints. See [the assessment](ecosystem.md).

Prospective differentiable integration, regulatory dynamics, explicit biological
constraints, and other custom operators need their own mathematical contracts,
reference behavior, gradient validation, and numerical error/stability analysis.
Choices include differentiating through discrete steps, implicit or adjoint
methods, and objectives that accommodate nondifferentiable transitions. Their
appropriateness depends on the experiment and available implementation.

## Execution and lifecycle boundaries

Karyoplast owns scientific model semantics and experiments. Cytoplast is intended
to execute/train shared numerical models across many instances; FrameShift is
intended to supply logical lifecycle, communication, and suspension/resumption.
CellShard may supply storage/delivery. Device Scheduler allocates physical
resources outside model semantics.

Potential boundary questions include opaque versus structured cell state,
model/genome revisions, execution inputs/outputs, time and causality, messages,
snapshot compatibility, cancellation, resource loss, gradient aggregation, and
optimizer ownership. These are questions, not API declarations. FrameShift's
existing typed agent contracts and Cytoplast's conceptual contracts must be
assessed against a real numerical consumer before Karyoplast defines adapters.
