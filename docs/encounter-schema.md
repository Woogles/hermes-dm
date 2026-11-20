# Encounter Schema (v1)

## Purpose

Describes a single **moment of pressure** the party can face inside an
adventure. Encounters are not the whole session, they are one beat:
a chase, a confrontation, a ritual, a hazard, a combat, or a boss.

## File location

`campaigns/<campaign-id>/encounters/<encounter-id>.yaml`

Filename must equal id. Registered in `campaign.yaml → resources →
encounters`.

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | kebab-case unique id |
| `type` | enum | what kind of beat this is (see below) |
| `level_range` | string | `"X-Y"` |

## Optional but recommended fields

| Field | Type | Meaning |
|---|---|---|
| `tone` | enum | `low` `moderate` `high` `unstable` `extreme` |
| `goal` | text | one sentence: what the party is doing here |
| `objective` | text | alternate label for `goal` |
| `enemies` | list of npc-ids | who is present |
| `major_threat` | list of npc-ids | what the party must respect |
| `minor_threat` | list of npc-ids or names | background nuisance |
| `player_options` | list | the actions they can take |
| `options` | list | alias for player_options |
| `lesson` | text | what they should learn |
| `failure_consequence` | text | what happens if they fail |
| `success_text` | text | what happens if they succeed |
| `special` | text | one-off rules for this beat |
| `hazards` | list of text | environmental effects |
| `effects` | list of text | mechanical effects on the party |
| `boss` | list of npc-ids | if this is a boss beat |

## Allowed `type`

Compound names are formed as **primary-subordinate**. The primaries are:

    combat
    skill-challenge
    social
    ritual
    hazard
    chase
    boss
    paradox

Use one primary and add a second if it blends two kinds. Examples:
`social-combat`, `skill-challenge-combat`, `combat-social`, `paradox-boss`,
`chase-social`, `light-combat-skill`, `ritual-skill`.

## Example (real, from vanished-century)

    encounter:
      id: echo-warden-confusion
      type: skill-challenge-combat
      level_range: "1-4"
      major_threat:
        - Echo Warden
      minor_threat:
        - Grotto Runner
      lesson: >
        Use Insight or Arcana before attacking.
      failure_consequence: >
        The party learns the cause is magical, but does not fully
        stabilize the echo.

## Author checklist for a new encounter

1. Decide the **primary type** first. If it is combat-heavy, the campaign
   is probably not beginner.
2. Set `tone`. Low = chase/witness. Moderate = talk or short fight.
   High = ritual or faction confrontation. Extreme = final paradox beat.
3. Give the party at least two `player_options`. Always include a
   non-combat option.
4. Write `failure_consequence` as a state change, not a death:
   "the witness leaves, but the paradox rises."
5. Reference NPC ids that already exist in this campaign's `npcs/` folder.

## Cross-references

- `enemies`, `major_threat`, `minor_threat`, `boss` must reference
  **existing** npc ids from the same campaign.
- `type: paradox-boss` should appear in an `adventure` that is also
  in `act 3` or a late `act`.
- Encounter ids appear in `campaign.yaml → resources → encounters`.

## Common mistakes

- Writing a whole session as one encounter. That is an `adventure`,
  not an `encounter`.
- Setting a beginner campaign's tone to `extreme`.
- Making `failure_consequence` "everyone dies". Fail forward.
- Referring to an NPC by **name** ("Echo Warden") instead of by **id**
  (`echo-warden`) inside `enemies` and `boss` lists. Ids are for code.