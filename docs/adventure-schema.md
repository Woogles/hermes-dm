# Adventure Schema (v1)

## Purpose

Describes one playable unit the party can walk through in one to three
sessions. An adventure is the smallest repeatable story block. Each one
is also a **quest id**: when the party completes it, that id moves from
`active_quests` to `quests_completed`.

## File location

`campaigns/<campaign-id>/adventures/<adventure-id>.yaml`

Filename must equal id. The same id is registered in:
- `campaign.yaml → resources → adventures`
- `campaign.yaml → quests → quest_ids`
- one and only one `acts/*.yaml → adventures` list

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | kebab-case unique id (this is also the quest id) |
| `act` | integer | which act it belongs to |
| `level_range` | string | `"X-Y"` format (e.g. `"1-2"`) |
| `objective` | text 1–2 sentences | what the party is trying to find out |
| `major_clues` | list of 3–5 short phrases | the clues the party can use |
| `success_condition` | text | what counts as done |
| `failure_condition` | text | usually a runtime effect, e.g. `paradox +1` |

## Optional but strongly recommended fields

| Field | Type | Meaning |
|---|---|---|
| `skill_challenge` | list of `{check, dc, meaning}` | checks the party can roll |
| `known_on_success` | text | the fact the DM states when the party wins |
| `known_on_failure_with_plan` | text | the fact revealed even when they fail, if they explain their plan |
| `choices` | list of 2–3 options | the decision the party makes at the end |
| `simple_answer` | text | one sentence on the truth |
| `scene_template` | list | repeatable structure for multi-scene adventures |
| `paradox_risk` | list | if a rule breaks, what paradox escalates |
| `anchor_rule` | text | if an anchor is involved, what is safe |
| `echo_rule` | text | if an echo is involved, what separates Anchor from Echo |
| `ring_entry_rule` | list of `{cost, result}` | how the party enters a hidden layer safely |
| `social_challenge` | list | the questions the party must answer to a faction |
| `response_if_*` | text | outcomes keyed to social tone (cautious, dishonest, helpful) |
| `boss` | string or object | an NPC id (or `{id, statblock}`) |
| `final_boss` | object | final encounter with `name`, `recommended_statblock`, `goal` |
| `faction_conflicts` | list | factions that disagree about the truth |
| `hazards` | list | passive effects during the adventure |

## Allowed values for `failure_condition`

Use one of these templates:

- `paradox +1`
- `<faction> gains influence`
- `<faction> reacts`
- `<anchor> becomes unstable`
- `echo appears`
- `major paradox`
- `catastrophic collapse risk`

Do not use "game over", "TPK", or "the party dies". Fail forward.

## Example (real, from paper-circus)

    adventure:
      id: missing-ringmaster
      act: 1
      level_range: "1-2"
      objective: |
        Discover why the town remembers a ringmaster who does not
        appear in the ledger.
      major_clues:
        - poster with ringmaster
        - ticket says one show
        - witness remembers too perfectly
      success_condition: identify ringmaster memory
      failure_condition: paradox +1
      skill_challenge:
        - check: Investigation
          dc: 10
          meaning: find poster and ticket
        - check: History
          dc: 10
          meaning: compare memory to ledger
        - check: Insight
          dc: 12
          meaning: witness memory is too perfect

## Author checklist for a new adventure

1. Choose a title that reads as a **question**, not a statement:
   "missing-ringmaster" not "the ringmaster is missing".
2. Write 3 to 5 `major_clues` as short physical objects or witness
   phrases. Avoid abstract nouns.
3. Set one `success_condition` and one `failure_condition`. Never
   more than one each.
4. Give at least one `known_on_failure_with_plan` so failure still
   teaches something.
5. Use skill DCs that fit the level_range. Beginner = 10–13.
   Intermediate = 12–17. Advanced = 15–22.
6. Do not list "combat is the solution" as a condition. Use
   social/skill conditions; put combat in an `encounter` file.
7. Confirm the adventure id appears in `campaign.yaml → quests → quest_ids`
   AND `campaign.yaml → resources → adventures` AND exactly one
   `acts/*.yaml → adventures`.

## Cross-references

- `act` integer must match an existing `acts/act<N>.yaml` number.
- `boss` or `final_boss` id must exist in `campaign.yaml → resources → npcs`.
- `skill_challenge` check names must be real 5.5e skill names:
  `Investigation, History, Insight, Arcana, Religion, Persuasion,
   Nature, Performance, Survival, Perception, Athletics, Medicine,
   Sleight of Hand, Stealth, Animal Handling, Acrobatics`
- Adventure id == quest id. Never rename one without the other.

## Common mistakes

- Making every clue a noun like "the mystery". Clues should be things
  the party can *look at*: missing shelf, altered plaque, false ticket.
- Writing `success_condition: find the answer`. That is too vague.
  Use a specific action.
- Using `failure_condition: TPK`. That kills the fail-forward schema.
- Making an adventure belong to two acts. Each id lives in one act.