# Training and evaluation research

No dataset, objective, neural framework, optimizer, or training system is chosen.
The eventual target is population-level learning: observations and trajectories
from many interacting virtual cells improve one common parameter set.

## Candidate learning directions

Supervised temporal or perturbation-conditioned prediction could establish a
bounded baseline. Self-supervised objectives could use masked measurements,
cross-modal relations, temporal context, or trajectory consistency. Their
usefulness for autonomous behavior must be demonstrated rather than inferred
from representation quality alone.

Developmental training may require distributions over transitions, division and
branching trajectories, interaction-dependent changes, and variable population
sizes. Partial lineage information, uncertain time, destructive assays, and
unobserved environmental variables complicate supervision. A population
snapshot is not a measured individual history; inferred pseudotime is not a
directly observed physical trajectory.

Continuous components might support gradient-based rollout training through
validated scientific operators. Discrete division or interaction events might
need likelihood-based treatment, marginalization, stochastic estimators, or
other methods. None is selected. Gradient paths, approximation bias, memory,
numerical stability, and identifiability need explicit investigation.

Shared optimization must eventually specify how contributions from multiple
cells and lineages are weighted, how correlated relatives affect sampling, and
when cells adopt new parameter revisions. Cytoplast training support is
prospective, so no distributed optimizer contract should be assumed.

## An initial experiment proposal must state

1. A biological question and bounded target behavior, including omitted biology.
2. Dataset identity, provenance, access/license conditions, measurement process,
   units, time information, lineage/interaction evidence, and missing modalities.
3. A minimal state/observation representation, simple baselines, and candidate
   model/objective whose added complexity has a concrete purpose.
4. Splits at appropriate biological units (such as donors, experiments,
   conditions, or entire lineages) to limit leakage from related observations.
5. Prediction, dynamical, and uncertainty criteria; perturbation and repeated
   rollout tests; limits on supported mechanism or causal claims.
6. Reproducible CPU-first checks where possible, with resource authorization for
   any later GPU execution. This document does not authorize an experiment.

## Evaluation layers

| Layer | Questions and possible evidence |
| --- | --- |
| Observable prediction | Held-out error or likelihood, calibration, modality-specific measurement fit, comparison with simple baselines. |
| Repeated dynamics | Stability, uncertainty growth, plausible time scales, sensitivity to initial conditions, constraints and failure under long rollout. |
| Branching and inheritance | Lineage consistency, sister-cell dependence, daughter-state distributions, population size/composition and division timing where observed. |
| Interacting populations | Signal/neighbor dependence, spatial organization, distributions and trajectories, interaction ablations and held-out environments. |
| Perturbation and robustness | Responses under withheld interventions, recovery/failure behavior, distribution shift and uncertainty calibration. |
| Mechanistic or causal inference | Observability, identifiability, competing explanations, intervention evidence, and tests that can falsify a proposed mechanism. |

Evaluation must distinguish fitted observations from held-out trajectories and
independent perturbation evidence. Matching a developmental distribution does
not prove the underlying regulatory mechanism was recovered. A stable latent
model may be useful while remaining mechanistically ambiguous; GlassHelix can
inform what further observations distinguish alternatives. Synthetic fixtures
validate algorithms under stated assumptions, not biological validity.
