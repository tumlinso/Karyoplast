# Open scientific and architectural questions

All entries are unresolved. Their order is a navigation aid, not a plan commitment.

## State, observations, and time

- What is the minimal useful representation of cellular state for an initial
  scientific question? Which measurements and latent variables are necessary?
- How much structure should be learned versus supplied by Cellerator? Which
  transformations should be neural and which explicit mathematical operators?
- What constitutes a biological token, event, or generative step? Is tokenization
  useful at all for the selected experiment?
- How should continuous biological time, asynchronous events, multiple time
  scales, and observation times enter the model?
- What memory is necessary for persistent differentiation, and how can it be
  bounded, inherited, checkpointed, and tested?
- How should genomic sequence enter the model through Baseplane, while keeping
  exact sequence/provenance distinct from embeddings and learned weights?

## Dynamics, division, and interaction

- How should division produce distinct daughter states, correlated inheritance,
  lineage identity, and appropriate conservation constraints?
- How should environments, spatial organization, and intercellular signaling be
  represented? What can the available observations constrain?
- Which form of conditional computation or expert specialization is appropriate?
  What evidence would show that MoE adds value over a simpler shared model?
- How should scientific operations participate in gradient computation? Which
  forward, JVP, VJP, higher-order, or nondifferentiable paths are actually needed?
- Which numerical integration/stability properties and explicit biological
  constraints must be supplied, and which can usefully be learned?

## Learning and validation

- Which training objectives and datasets can support the intended dynamics,
  including temporal, perturbation, lineage, and interaction evidence?
- How should population observations update shared parameters without treating
  related cells as independent evidence or leaking lineages across splits?
- How should learned population development be validated under repeated rollout,
  interventions, held-out environments, and uncertainty?
- Which latent dynamics are observable or identifiable? What experiments can
  distinguish predictive alternatives before a mechanistic claim is justified?

## Cross-project contracts

- What should actual Cytoplast model/backend and cell-execution interfaces
  expose? How should gradients, optimizers, model revisions, and snapshots align?
- What should FrameShift expose for numerical state, time, communication,
  suspension/resumption, and lifecycle causality? Which existing typed/nontext
  contracts transfer, and which require new work?
- What CellShard storage/delivery capabilities are useful without duplicating
  Cytoplast execution or Device Scheduler resource authority?

Promote a question to a decision only with scope, rationale, evidence, and
reconsideration conditions in [the decision record](decisions.md).
