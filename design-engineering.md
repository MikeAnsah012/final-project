---
layout: default
title: Enhancement #1 — Software Design & Engineering
nav_order: 3
---

# Enhancement #1 — Software Design & Engineering

**Goal:** Improve maintainability, security, and delivery.

## What I Changed
- Separated concerns into **UI / API / Data Access** layers.
- Added **role‑based access control (RBAC)** and centralized **input validation** at the API boundary.
- Wrote **unit tests** (models, services) and **integration tests** (API endpoints + DB).
- Implemented **CI pipeline** (build → test → lint → image) and **Docker/compose** for reproducible environments.

## Skills Demonstrated
- SOLID principles, dependency injection, interface‑driven design
- Secure coding (validation, least privilege), testing strategy, CI/CD

## Evidence
- Architecture diagram and folder map (see `artifact-animal-shelter/docs/`)
- Test coverage report (target ≥ 80%)
- CI YAML + build badges (link your Actions runs)
- Dockerfile/compose and run instructions

## Program Outcomes Alignment
- Software engineering best practices; testing and QA; security fundamentals; effective communication via docs and diagrams.
