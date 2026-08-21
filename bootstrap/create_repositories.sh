#!/usr/bin/env bash
set -euo pipefail

# Safe repository bootstrap for the 12-repository Mathematics Research Ecosystem.
# Default mode is DRY RUN. Pass --execute to perform GitHub writes.
# Requires: gh CLI authenticated to an account with permission to create repos under OWNER.

OWNER="${OWNER:-Dossiya-SE}"
VISIBILITY="${VISIBILITY:-private}"
MODE="${1:---dry-run}"

if [[ "$MODE" != "--dry-run" && "$MODE" != "--execute" ]]; then
  echo "Usage: $0 [--dry-run|--execute]" >&2
  exit 2
fi

repos=(
  mathematics-foundations
  mathematical-models
  mathematical-examples
  mathematical-reproductions
  mathematical-skills-development
  mathematical-visualization-art
  mathematical-computing
  mathematical-verification
  mathematical-physics
  mathematical-engineering-applications
  mathematics-literature-atlas
  mathematics-research-lab
)

descriptions=(
  "Rigorous mathematical foundations: definitions, notation, theorems and derivations"
  "Complete mathematical model specifications and architectures"
  "Worked mathematical examples from elementary to research level"
  "Independent mathematical reproductions with quantitative error checks"
  "Structured mathematical mastery ladders and competency evidence"
  "Scientific mathematical visualization, geometry art and publication graphics"
  "Multi-language mathematical computing implementations"
  "Symbolic, numerical and formal mathematical verification"
  "Mathematical physics: mechanics, fields, dynamics and geometric methods"
  "Mathematics applied to engineering, infrastructure, resilience and sustainability"
  "Mathematical literature provenance, theorem lineage and citation atlas"
  "Experimental mathematical research: conjectures, prototypes and open questions"
)

if [[ "$VISIBILITY" != "private" && "$VISIBILITY" != "public" && "$VISIBILITY" != "internal" ]]; then
  echo "VISIBILITY must be private, public, or internal." >&2
  exit 2
fi

for i in "${!repos[@]}"; do
  full="$OWNER/${repos[$i]}"
  if gh repo view "$full" >/dev/null 2>&1; then
    echo "SKIP existing: $full"
    continue
  fi

  echo "PLAN create: $full [$VISIBILITY]"
  if [[ "$MODE" == "--execute" ]]; then
    gh repo create "$full" "--$VISIBILITY" --description "${descriptions[$i]}" --disable-issues=false
  fi
done

if [[ "$MODE" == "--dry-run" ]]; then
  echo "DRY RUN complete. No repositories were created. Re-run with --execute after review."
else
  echo "Repository creation pass complete. Review GitHub before splitting or migrating content."
fi
