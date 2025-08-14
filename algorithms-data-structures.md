---
layout: default
title: Enhancement #2 — Algorithms & Data Structures
nav_order: 4
---

# Enhancement #2 — Algorithms & Data Structures

**Goal:** Make search, ranking, and assignment fast and meaningful.

## What I Built
- **Adoptability score**: weighted sum of normalized features (age, temperament, training history, health flags) → 0–100.
- **Kennel assignment**: greedy heuristic using priority queues to place high‑score dogs into limited capacity with compatibility constraints.
- **Caching**: LRU map for common filter queries; cache invalidates on CRUD.
- **Efficient search**: moved to **indexed, compound filters** and short‑circuit logic.

## Complexity Notes
- Ranking: O(n) per batch
- Assignment: O(n log n) with a priority queue
- Cache: O(1) average get/put; bounded memory

## Evidence
- Pseudocode + key code excerpts
- Before/after latency table (e.g., 420ms → 85ms average on common filters)
- Unit tests for scoring, assignment, and cache invalidation

## Program Outcomes Alignment
- DSA mastery, performance tuning, and practical optimization under real constraints.
