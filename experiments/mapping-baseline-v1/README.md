# Mapping Baseline v1

## Purpose

Reproduce a portfolio-safe GRC Mapping experiment using a sanitized directed relationship graph and deterministic analysis.

## Research question

Can the GRC Mapping Model expose structural conditions that a conventional control crosswalk would not make obvious?

## Baseline analyses

1. Build a directed graph from canonical objects and typed relationships.
2. Identify articulation points and bridges.
3. Measure degree centrality and connected components.
4. Perturb selected nodes and relationships.
5. Compare survival ratios and fragility classifications.
6. Record outputs as reproducible result artifacts.

## Input boundary

Use only sanitized data suitable for public demonstration. Do not copy protected mappings, scoring rules, evidence, or calibration thresholds from the private research environment.

## Reproduction sequence

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn grc_analysis_engine.api.app:app --reload
```

Use `data/sample_graph.json` as the initial baseline graph.

## Expected outputs

- Topology findings
- Critical nodes / articulation points
- Critical relationships / bridges
- Robustness and sensitivity results
- A short interpretation explaining what changed under perturbation

## Provenance

This experiment operationalizes the public GRC Mapping Model described in the GRC Atlas. Protected calibration and multi-framework validation are performed separately in GitLab.
