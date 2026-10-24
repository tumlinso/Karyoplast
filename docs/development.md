# Development and evidence

## Package foundation

The scaffold uses the standard `src/` layout and setuptools, targets Python
3.10+, and has no runtime dependencies. Only package identity is implemented.
There is no model, CLI simulator, state abstraction, trainer, or native build.
Licensing has not been selected; no license grant is asserted by package metadata.

```sh
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

For editable development, use the virtual environment instructions in the
[README](../README.md). In an offline environment with a compatible setuptools
already installed, `python -m pip install --no-deps --no-build-isolation -e .`
avoids downloading build requirements. Validate installed imports from outside
the checkout so a source-path import cannot hide a packaging defect.

Minimal changes need proportionate checks. Scaffold tests establish import and
package metadata behavior only. Later numerical operators require independent
references and appropriate derivative/numerical validation; biological claims
need experimental evidence beyond software tests.

## Organization

| Location | Contents |
| --- | --- |
| `src/karyoplast/` | Python package source, initially only package identity. |
| `tests/` | Small focused checks; no GPU or data downloads in scaffold tests. |
| `docs/` | Scientific intent, alternative designs, integration evidence, development guidance. |
| `docs/evidence/` | Small dated inspection and validation records with provenance. |
| `planning/` | Provisional roadmap, unresolved questions, decision rationale, later reviewable plan inputs. |
| Local `data/`, `datasets/`, `checkpoints/`, `runs/`, `outputs/` | Ignored large/generated artifacts; keep provenance and small evidence records in tracked documentation. |

## Recording claims and decisions

Separate intention, source presence, executed behavior, numerical validation,
predictive validation, and mechanistic interpretation. Record the source
revision and any uncommitted-source digest when citing neighboring interfaces;
their presence is not an installation or interoperability guarantee.

For experiments retain dataset/split identities, preprocessing and units, time
conventions, seeds, commands, environment/dependency versions, precision,
checkpoint/model revision, outputs or durable artifact locators, and limitations.
For a consequential decision record its status, alternatives, rationale,
evidence, and conditions for reconsideration. Keep deferred hypotheses visible.

Use Project Control for registered context and supported workflow state where
configured. Do not turn exploratory documents into active tasks without an
explicit plan-adoption step. Never hand-edit authority SQLite or generated
Todo projections. Preserve independent neighboring repositories and resource
authority boundaries.
