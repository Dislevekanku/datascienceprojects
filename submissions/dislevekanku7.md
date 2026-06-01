# Agentic Data Passbooks: A Verification Layer for Coordinating Through AI Agents

Authors: Disleve Kanku (OncoSys AI / Northeastern University)
Contact: dislevekanku7@gmail.com
Type: Note
Track: TR.04
Word count: 340
Keywords: algorithmacy, AI agents, data governance, verification, provenance, trust infrastructure
Conflicts of interest: none

---

## Abstract

As workers increasingly coordinate through AI agents, the central challenge is no longer only whether humans can understand algorithms, but whether they can verify the data, assumptions, and authority behind agentic decisions. This note introduces Agentic Data Passbooks as a practical trust layer for algorithmic coordination: structured, machine-readable records that describe what data an agent can access, what guarantees are attached to that data, and what evidence supports those guarantees.

The contribution is a framework for moving from AI literacy to AI verifiability. In many workplaces, algorithmic third parties now mediate handoffs between humans: a clinician and a data steward, a researcher and an analytics platform, a manager and an automated workflow, or one AI agent negotiating with another. These interactions require more than prompt engineering or user training. They require a shared protocol for checking provenance, schema, freshness, lineage, sensitivity, access rights, and quality before an AI-mediated action is trusted.

Drawing from work in healthcare data infrastructure, oncology real-world data readiness, and multi-agent systems research, this note proposes passbooks as coordination artifacts. A passbook does not store raw data. Instead, it exposes metadata, compute capabilities, validation checks, access policies, and runtime guarantees that allow agents and humans to reason about whether a data asset is fit for a given task. In regulated environments, this becomes especially important because the cost of opaque coordination is high: incorrect downstream decisions, unverifiable evidence chains, and brittle trust in automated systems.

The paper situates Agentic Data Passbooks within the broader concept of algorithmacy. If algorithmacy is the competency of coordinating with another human through an algorithmic third party, then passbooks help define what competent coordination requires in agentic systems: not blind reliance, but structured verification. The note outlines an architectural pattern involving Agent Facts, Data Facts, compute functions, signed metadata, and runtime validation. It also discusses how this pattern could support healthcare research, enterprise workflow automation, and public-interest AI systems.

The goal is to give practitioners, researchers, and system designers a concrete vocabulary for building AI-mediated work that is inspectable, governable, and accountable.

## Outline

1. Algorithmacy and the shift from human-tool interaction to human-agent-agent-human coordination
2. Why AI literacy is insufficient without verification infrastructure
3. The trust problem in agentic data access: provenance, schema, freshness, quality, lineage, and sensitivity
4. Agentic Data Passbooks as structured coordination artifacts
5. Architecture: Agent Facts, Data Facts, compute capabilities, access policies, and runtime validation
6. Healthcare and oncology data readiness as a high-stakes use case
7. Implications for governance, worker agency, and accountable AI-mediated work
8. Future directions for open standards and empirical evaluation

## Author bios

Disleve Kanku is the Founder of OncoSys AI and an AI/data systems builder working at the intersection of healthcare data infrastructure, agentic systems, and trustworthy AI. He has experience building data pipelines and governance workflows in clinical and research environments and is currently researching verifiable data access architectures for multi-agent systems.

## Methods (optional)

This note is based on design research and systems architecture work involving healthcare data infrastructure, agent-mediated access patterns, and verification requirements for regulated data environments.

## Data & artifacts (optional)

Artifacts are forthcoming and may include architectural diagrams, example passbook schemas, and prototype validation flows.

## Statement on review policy

By submitting, I/we acknowledge that this submission and all reviews of it will be public on this repository under the conference's open-review policy.
