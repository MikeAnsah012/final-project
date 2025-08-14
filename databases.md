---
layout: default
title: Enhancement #3 — Databases
nav_order: 5
---

# Enhancement #3 — Databases

**Goal:** Make the data layer robust, validated, and insightful.

## What I Implemented
- **JSON Schema validation** on `animals` to prevent malformed documents.
- **Indexes**: compound `{ breed: 1, age: 1 }`, **text** on `notes`, and **2dsphere** on `location`.
- **Aggregation pipelines**: candidate lists, KPI rollups (counts by breed/age/region), and training conversion rates.
- **Explain plans** to verify index usage; **backup/restore** scripts and a brief **data lineage** note.

## Evidence
- `mongosh` scripts, schema JSON, `db.collection.getIndexes()`, and `db.collection.explain()` outputs
- Aggregation pipeline samples
- Screenshot of dashboards reflecting aggregated results

## Program Outcomes Alignment
- Database modeling, indexing strategy, analytics with aggregations, reliability, and governance.
