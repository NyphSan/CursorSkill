# CODEX_HANDOFF

## Project Goal

Maintain and publish the `gamestudio` Codex skill as a practical full-game workflow.

## Current Phase

- Phase: Skill refinement
- Status: Mobile game UI/UX quality gate implemented, validated, and synced to the installed skill

## Latest Completed Work

- Added mandatory mobile UI/UX audit triggers and non-negotiable HUD/readability rules.
- Added a dedicated `references/ui-ux-audit.md` audit workflow and output format.
- Documented the new quality gate in Chinese and English README files.
- Synced `SKILL.md` and `references/ui-ux-audit.md` to `C:\Users\test\.codex\skills\gamestudio`.

## Important Modified Files

- `SKILL.md`
- `references/ui-ux-audit.md`
- `README.md`
- `README.en.md`

## Verification

- Official `quick_validate.py`: `Skill is valid!`
- `git diff --check`: passed
- Source and installed `SKILL.md` / `ui-ux-audit.md` SHA-256 hashes: matched

## Known Risks

- Heuristic font and touch guidelines still require device/runtime evidence for each game.

## Next Safest Task

Validate the skill, sync the installed copy, commit the scoped files, push `main`, and verify the remote hash.
