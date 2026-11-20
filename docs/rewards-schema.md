# Rewards Schema (v1)

Defines `rewards.yaml`. A small structured file that lists which items the
campaign hands out and why. It keeps the reward layer from being free-form
and ties it to the `items/` folder + `runtime_variables`.

## File location

`campaigns/<campaign-id>/rewards.yaml` (exactly one per campaign)

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `rewards` | list of ids | ids that MUST exist in `campaigns/<id>/items/` |
| `summary.reward_type` | enum | `campaign-artifacts` \| `story-items` \| `investigation-tools` \| `consumables` \| `mixed` |
| `summary.goal` | text 1 sentence | what these rewards let the party do |

## Optional fields

| Field | Type | Meaning |
|---|---|---|
| `per_act` | map actN → [ids] | which rewards unlock at which act |
| `beginner_only` | list of ids | items gated to beginner difficulty |
| `advanced_only` | list of ids | items gated to advanced |
| `gated_by_quest` | map quest-id → [ids] | reward after finishing a quest |

## Allowed `summary.reward_type`

`campaign-artifacts` | `story-items` | `investigation-tools` | `consumables` | `mixed`

## Rules

- every id in `rewards` must exist in `items/` AND be in
  `campaign.yaml resources.items`.
- any reward that consumes a token/key must have a matching integer
  runtime variable in `campaign.yaml runtime_variables`.
- rewards listed in `per_act` reference acts that exist in
  `campaign.yaml resources.acts`.

## Example (vanished-century)

    rewards:
      - witness-notebook
      - case-lens
      - ring-anchor-token
    summary:
      reward_type: investigation-tools
      goal: give beginners simple investigative tools without complex magic.
    per_act:
      act1: [witness-notebook]
      act2: [case-lens]
      act3: [ring-anchor-token]

## Author checklist for a new rewards.yaml

1. List ids that actually exist in `items/`.
2. Pick `reward_type` honestly — if it contains a permanent artifact use
   `campaign-artifacts` or `mixed`, not `consumables`.
3. If a reward spends a token, confirm the token runtime variable exists.
4. For beginner campaigns: ≤3 rewards, all `visible_to_players`-safe tools.

## Cross-references

- id ⇄ `campaign.yaml resources.items` ⇄ `items/<id>.yaml`.
- `gated_by_quest` ids ⇄ `campaign.yaml quests.quest_ids`.

## Common mistakes

- Listing a reward with no item file → loader fails "dangling id".
- Calling a permanent Loom a "consumable".
- Putting an item in rewards but not in `resources.items`.
- Giving a beginner campaign five complex artifacts.