# GRC Analysis Engine

Version **0.1.0** establishes the deterministic analytical core for the GRC Mapping Model and Governance Intelligence research program.

> **Repository posture:** Private research/development repository. Public disclosure should remain at the capability and milestone level unless specific implementation details are intentionally released.

## Design principles

1. **Deterministic first.** Structural findings are reproducible and do not depend on an LLM.
2. **Graph-provider agnostic.** Analytical modules operate on an internal `GovernanceGraph` contract, not directly on Neo4j.
3. **Evidence-aware.** Relationships carry confidence, strength, criticality, propagation potential, and optional seam metadata.
4. **Inspectable.** Every analysis returns structured results that can later be persisted as auditable analysis runs.
5. **Expandable.** Topology and robustness are the first modules; propagation, seams, assurance, and confidence modeling follow.

## v0.1 modules

- Canonical node and relationship models
- NetworkX-backed graph implementation
- Topology analysis
  - articulation points
  - bridges
  - degree centrality
  - connected components
- Relationship robustness / sensitivity analysis
  - baseline connectivity
  - edge perturbation
  - node perturbation
  - survival ratio
  - fragility classification
- FastAPI interface
- Sample governance graph
- Automated tests
- Neo4j adapter boundary (stubbed for the next integration pass)

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn grc_analysis_engine.api.app:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## API endpoints

- `GET /health`
- `POST /analysis/topology`
- `POST /analysis/robustness`

The POST endpoints accept the same graph payload: nodes plus directed relationships.

## Example relationship

```json
{
  "id": "REL-0001",
  "source": "GOV-001",
  "target": "PROC-001",
  "relationship_type": "GOVERNS",
  "strength": 0.95,
  "confidence": 0.90,
  "criticality": 0.85,
  "propagation_potential": 0.80,
  "seam_type": "governance-to-process"
}
```

## Roadmap

### AE-01 — Relationship Robustness & Sensitivity
Current module. Expand to weighted confidence sensitivity, alternate-path resilience, and pathway-level perturbation.

### AE-02 — Propagation
Directed impact propagation, decay, thresholds, and affected-domain analysis.

### AE-03 — Seam Analysis
Translation-loss and meaning-fidelity scoring across governance seams.

### AE-04 — Assurance
Requirement → responsibility → control → evidence → validation → assurance pathways.

### AE-05 — Governance Confidence Modeling
Relationship confidence, evidence confidence, pathway confidence, and system confidence.

### AE-06 — Neo4j / GDS
Persistent graph store and large-scale graph analytics while preserving the provider-neutral engine interface.
