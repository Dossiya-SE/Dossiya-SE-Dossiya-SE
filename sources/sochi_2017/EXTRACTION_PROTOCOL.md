# High-Rigor Extraction Protocol — Sochi Differential Geometry Foundation

## Source identity

- **Source ID:** `SOCHI-DG-2017-UPLOADED`
- **Author:** Taha Sochi
- **Title:** *Introduction to Differential Geometry of Space Curves and Surfaces*
- **Internal date evidence:** Preface signed “London, March 2017”.
- **User-supplied file:** `2501.0039v1.pdf`
- **PDF extent:** 252 pages.
- **Pagination rule:** printed book page `p` corresponds to PDF page `p+1` from printed page 1 onward because PDF page 1 is the cover.

No publication venue, DOI, ISBN, edition statement, or license is asserted here unless independently verified later. The uploaded PDF is treated as the primary source artifact for this extraction.

## Purpose

This protocol converts the book into a traceable mathematical foundation without turning the repositories into a copy of the book. Each module receives only the material needed for its unique scientific function.

## Extraction classes

Every extracted item must be labeled conceptually as one of:

1. **DEF** — definition or terminology.
2. **EQ** — mathematical equation or identity.
3. **THM** — theorem or named mathematical result.
4. **COND** — domain, regularity, differentiability, or existence condition.
5. **EX** — worked geometric example or parameterization.
6. **VIS** — source figure used only as a reconstruction target.
7. **SKILL** — exercise or competency anchor.
8. **LIMIT** — scope limitation stated or directly implied by the source.
9. **EXT** — repository extension not claimed to come from the book.

## Required provenance fields

Stable artifacts derived from the book must record, when applicable:

- `source_id`;
- chapter and section;
- printed page or page range;
- PDF page or page range;
- source equation number, theorem name, exercise number, or figure number;
- whether notation is preserved or normalized;
- whether the artifact is a direct mathematical extraction, paraphrase, reconstruction, verification, or extension;
- assumptions and domain restrictions;
- verification status.

## Mathematical transcription rules

1. Never silently repair an equation whose parsed-text transcription is uncertain.
2. If an equation is used in executable code, compare it against the rendered PDF page before promotion to `verified`.
3. Preserve the book's sign convention when reproducing a source result; if another convention is used, document the transformation explicitly.
4. Preserve parameter domains. Examples: torus requires `r < R`; pseudosphere parameterization requires `0 < theta < pi`; regular curves require nonzero velocity where stated.
5. Distinguish surface Greek indices from space Latin indices when using the book's tensor notation.
6. Do not infer an engineering interpretation from a geometric quantity without marking it `EXT`.

## Copyright-safe repository rule

The repository stores compact paraphrases, mathematical formulas, metadata, source anchors, independently written code, and regenerated figures. It does **not** reproduce the book's prose chapter-by-chapter and does **not** copy the original figures. Visual artifacts must be regenerated from mathematical parameterizations or independent implementations.

## Verification ladder

`extracted -> transcribed -> implemented -> numerically checked -> invariant checked -> independently reproduced`

Promotion beyond `transcribed` requires at least one machine-checkable or analytic check when such a check is meaningful.

## Scope boundary of the source

The preface describes the book as an intermediate treatment of differential geometry of space curves and surfaces, largely through tensor calculus. It assumes broader mathematical background and explicitly says its preliminary mathematical background is not comprehensive. Therefore this source is a **primary foundation for curve/surface differential geometry**, not a universal foundation for all mathematics, all Riemannian geometry, topology, numerical analysis, physics, or engineering.
