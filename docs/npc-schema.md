# NPC Schema (v1)

## Purpose

Describes a single character the party can meet, talk to, fight, or
investigate. Every major character in a campaign is one YAML file here.

## File location

`campaigns/<campaign-id>/npcs/<npc-id>.yaml`

Filename must equal the id.

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | kebab-case unique id for this NPC |
| `name` | string | display name the DM reads aloud |
| `faction` | string | references a faction id declared elsewhere |
| `importance` | enum | `major` or `minor` |
| `disposition` | enum | how NPC behaves toward the party (see enum below) |
| `secrets` | integer 1–5 | how many hidden layers of mystery this NPC represents |
| `first_appearance` | string | adventure id (also a quest id) where they first appear |

## Optional fields

| Field | Type | Meaning |
|---|---|---|
| `role` | text 1–2 sentences | one-line job of this NPC in the story |
| `behavior` | list | repeated actions, phrases, or tactics they will use |
| `lesson` | text | what the party should learn from engaging them |
| `insight_on_success` | text | payoff for an Insight check |
| `arcana_on_success` | text | payoff for an Arcana check |
| `options` | list | how the party can interact (talk, prove, fight, flee) |
| `clue` | text | a single clue they hand out |
| `social_rule` | text | how a faction reacts if the party is dishonest |
| `final_choice` | list | last-act decision options this NPC forces |
| `non_tpk_rule` | text | what happens if the party loses against them |

## Allowed values

**importance** = `minor` | `major`

**disposition** =
`cautious` (does not attack unless provoked),
`curious` (watches, may flee),
`friendly` (open to cooperation),
`hostile` (attacks or antagonises),
`mischievous` (tricks, moves things, does not fight)

**secrets** = 1 to 5. Higher = more hidden layers (1 = one secret, 5 = final-boss tier).

## Example (real, from vanished-century)

    npc:
      id: echo-warden
      name: Echo Warden
      faction: unseen-century
      importance: major
      disposition: cautious
      secrets: 3
      first_appearance: library-no-exit
      role: >
        Confuses witnesses and tests whether they remember the same event.
      behavior:
        - uses reactions to confuse witnesses
        - creates one fake echo
        - cannot fight for too long
      lesson: >
        Use Insight or Arcana before attacking.
      insight_on_success: >
        You realize the Echo Warden is not attacking people. It is
        testing whether witnesses remember the same event.
      arcana_on_success: >
        You find that its magic leaves tiny frost marks on old records.

## Author checklist for a new NPC

1. Pick an id and confirm it is unique across the whole campaign.
2. Pick a disposition that matches what you want the party to *do*, not what
   you want them to *fight*.
3. Set `secrets` to a number that fits the campaign's runtime: `secrets: 5`
   for a final boss, `secrets: 1` for a throwaway witness.
4. Make `first_appearance` reference an **existing** adventure id in
   `campaign.yaml → resources → adventures`.
5. Make `faction` reference an **existing** faction file in the campaign.
6. Give the party at least one non-combat way to engage them (`options`,
   `lesson`, `insight_on_success`).

## Cross-references

- `faction` → must match a `<campaign-id>/factions/<faction-id>.yaml`
- `first_appearance` → must match `<campaign-id>/adventures/<id>.yaml`
- The NPC id appears in:
  - `campaign.yaml → resources → npcs: [<npc-id>]`
  - any `encounter`'s `enemies`, `major_threat`, `boss` lists

## Common mistakes

- Using `id: EchoWarden` (must be kebab-case: `echo-warden`)
- `first_appearance: act1` (wrong — must be an **adventure** id, not an act)
- Making every NPC hostile. Most of your party engagement should be social.
- Giving an NPC no `lesson` or `options`. That turns them into a combat pinata.