# Scientific vision

## Long-term objective

Learn a generative representation of cellular functioning sufficiently complete
for one simulated founder cell to sustain itself and produce a developing
population. A cell should retain history, respond to its environment, communicate,
divide, and differentiate under the same learned parameters used by other cells.
Population organization should arise through interacting dynamics, potentially
including spatial constraints, local signaling, resource competition, and
multicellular phenomena.

This demands more than matching plausible gene-expression profiles. Persistent
behavior needs internal dynamics and interactions that remain coherent over
time. Division must connect mother and daughter states and lineages. Inheritance
may include conserved quantities, asymmetric molecular state, memory, and
environmental context; the correct representation is a research question.

The common model is the computational genome. Its training should eventually
draw information from populations of independent executions rather than assign a
different learned model to each differentiated cell. State and experience may
support specialization, but the mechanism and sufficiency of such memory are
unproven. A KV-cache analogy suggests persistence; it does not select a transformer
or establish that a cache captures biological memory.

## Initial scientific scope

Initial work should identify one bounded transition problem with interpretable
inputs, observations, time conventions, and validation criteria. For example, a
restricted perturbation response or short temporal transition might be useful
if an appropriate dataset and baseline support it. Neither is selected here.
An initial experiment need not include division, full spatial organization, or
a complete embryo.

Success in a small problem would establish only that component's predictive and
dynamical evidence. Expanding coverage requires explicit decisions about what
is omitted, how omitted variables affect the result, and which new observations
or experiments can constrain them.

## Observations, dynamics, and mechanism

Measurements sample a limited, noisy view of a living cell. Expression,
accessibility, protein abundance, signaling, metabolism, and spatial context
have different measurement processes and temporal scales. Snapshot collections
do not by themselves reveal single-cell trajectories or causal transitions.
Latent or unobserved processes may be essential even when their variables are
not directly measurable.

A model that reproduces developmental distributions may do so through several
different hidden dynamical systems. Predictive success supports prediction in
the tested domain; it does not uniquely recover the regulatory mechanism.
Mechanistic claims require additional observability/identifiability analysis,
competing explanations, interventions, and uncertainty assessment. GlassHelix
is relevant to these questions, without making them automatically solved.

The program should retain useful prediction even when mechanism remains
ambiguous, while making that ambiguity inspectable. Biological names for latent
coordinates, experts, or dependencies need evidence rather than analogy.
