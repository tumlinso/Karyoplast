# Representational foundations

## Three distinct objects

| Object | Initial expectation | Distinction to preserve |
| --- | --- | --- |
| Shared learned parameters | Numerical, predominantly floating-point trainable weights | The computational genome; shared across executions. |
| Simulated cell state | Vectors, tensors, latent memory, and possibly structured biological variables | Different per cell; evolves during execution and may be inherited at division. |
| Represented biological genome | Potential exact sequence, annotations, variants, or learned sequence representations | Biological information supplied to or represented by the model, not its trainable weights. |

Observable molecular measurements are another object: a noisy, partial readout
of biological state. The mapping between latent state and measurements must be
specified and tested; a latent coordinate is not automatically a particular
gene, molecule, or causal mechanism.

No decision requires neural weights to be strings of bases. Chromosomes are a
loose analogy for structured or conditionally used parameter groups. Experts,
if adopted, belong to the shared model; virtual cells are independent executions
of that model. A precision policy, tensor layout, tokenization, and parameter
partition scheme have not been selected.

## Alternatives to investigate

- Gene expression may be modeled as counts, transformed values, distributions,
  or learned embeddings. Units, noise, library-size effects, and observation
  assumptions matter to any choice.
- Chromatin state, signaling, proteins, metabolism, and other variables may use
  explicit biological axes, learned latent representations, or a combination.
  Missing modalities should not silently be treated as absent biology.
- Continuous latent dynamics may coexist with discrete division, contact,
  differentiation-related events, or state-dependent transitions. Continuous
  biological time need not equal one software step or one model invocation.
- Explicit structure can express constraints and interpretable relations;
  learned structure can represent unknown dynamics. Their division of labor
  should be tested rather than fixed by metaphor.
- Persistent state might be recurrent memory, a state-space vector, a context
  history, or a structured hybrid. A KV cache is only one analogy and may be
  unsuitable for long time scales, division, or repeated rollout.

These are candidates, not a chosen schema. The minimal useful state should be
defined against a specific experimental question and measurement process.

## Genomic grounding through Baseplane

Baseplane aims to combine exact genomic sequence with hierarchical learned
floating-point representations. Possible Karyoplast uses include conditioning
cellular dynamics on sequence-derived context, representing variants, or
constraining regulatory relationships. No Karyoplast adapter or trained
genome-wide encoder is established by this initialization.

Exact discrete sequence and continuous learned representations are compatible:
an encoder can consume exact bases while producing learned numerical features,
and exact sequence/provenance can remain available alongside those features.
Even if sequence becomes central, model weights remain numerical learned
parameters. Questions about coordinates, alleles, annotation provenance,
sequence updates, and gradient paths need consumer experiments and actual
Baseplane interface inspection before a contract is chosen.
