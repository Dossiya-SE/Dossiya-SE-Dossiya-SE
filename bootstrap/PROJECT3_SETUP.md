# GitHub Project 3 integration plan

Project URL supplied for this ecosystem: `https://github.com/users/Dossiya-SE/projects/3`.

## Important GitHub model

A GitHub Project is a control plane for issues and pull requests; repositories remain independent. Do not try to make Project 3 a parent folder for repositories.

## Project fields

Recommended fields:

- Domain
- Subdomain
- Repository
- Artifact Type
- Status
- Difficulty
- Rigor Level
- Programming Language
- Verification Level
- Reproduction Status
- Application Domain
- Priority
- Research Readiness
- Publication Readiness

Recommended Artifact Type values:

`Definition, Formula, Theorem, Proof, Derivation, Model, Example, Reproduction, Visualization, Algorithm, Software, Experiment, Application, Paper`

Recommended Status values:

`Idea, To Learn, Learning, To Derive, Deriving, To Implement, Implementing, To Verify, Verifying, Validated, Research Ready, Publication Ready`

## Repository creation

`create_repositories.sh` is intentionally dry-run by default. Review the manifest, then run:

```bash
VISIBILITY=private ./bootstrap/create_repositories.sh --dry-run
VISIBILITY=private ./bootstrap/create_repositories.sh --execute
```

The connected ChatGPT GitHub interface used to prepare this bootstrap does not currently expose repository creation/renaming or GitHub Projects v2 field editing, so those two operations are not silently simulated.

## Migration rule

After the twelve repositories exist, migrate one top-level module at a time. Preserve:

1. the artifact schema;
2. README scientific contract;
3. tests relevant to the module;
4. provenance files;
5. issue/PR references;
6. commit traceability where practical.

Do not delete the bootstrap repository until every target repository has been audited and the Project 3 links have been checked.
