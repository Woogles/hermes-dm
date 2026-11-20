# Faction Schema (v1)

## Purpose

Describes a group, institution, or world-force that the party can earn
trust with or anger. Factions are the social layer of the campaign;
they drive how the DM reacts to the party's tone.

## File location

`campaigns/<campaign-id>/factions/<faction-id>.yaml`

Filename must equal id. Registered in `campaign.yaml → resources →
factions`.

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | kebab-case unique id |
| `name` | string | display name |
| `alignment` | enum | two-word D&D alignment (see below) |
| `description` | text 1–2 sentences | who they are and what they want |
| `relationship_scale` | object | three integers keyed `trusted / neutral / hostile` |

## Optional fields

| Field | Type | Meaning |
|---|---|---|
| `enemies` | list of faction-ids | factions they dislike |
| `allies` | list of faction-ids | factions they support |
| `services` | list of strings | what the party can ask for |
| `enforcement_rule` | text | how they react to dishonesty |
| `reward_rule` | text | what they give when the party is honest |
| `influence_default` | integer | starting influence value if this faction has a runtime variable |

## Allowed `alignment` values (9-point D&D 2024)

    lawful-good lawful-neutral lawful-evil
    neutral-good neutral-neutral neutral-evil
    chaotic-good chaotic-neutral chaotic-evil

## `relationship_scale` rules

Three keys, exactly these names:

    trusted: positive (recommend +100)
    neutral: 0
    hostile: negative (recommend -100)

The scale is what the party's `runtime_variables` uses. A faction whose
runtime variable is, e.g., `silver_council_trust` uses
`trusted=100 / hostile=-100`.

## Example (real, from last-ferry)

    faction:
      id: fog-ledger
      name: Fog Ledger Society
      alignment: neutral-evil
      description: >
        A shady harbor society that buys impossible ferry memories,
        sells false tickets, and plants evidence in old ledgers.
      relationship_scale:
        trusted: 100
        neutral: 0
        hostile: -100

## Author checklist for a new faction

1. Ask: what does the party **do** with this faction? They can buy,
   steal, worship, repair, escort, report, or cooperate. If they can
   do nothing, it is not a faction, it is an NPC.
2. Set alignment to match what they want, not their flavor. A
   benevolent rebel gang is `chaotic-good`, not `chaotic-neutral`.
3. Keep description to 1–2 sentences. Do not put plot in the faction
   file.
4. If the faction has a runtime variable, define it in `campaign.yaml
   → runtime_variables` and set `influence_default` here.
5. Do **not** give factions their own secret list. Secrets belong to NPCs.

## Cross-references

- The faction id appears in:
  - `campaign.yaml → resources → factions`
  - every `npc`'s `faction:` field
  - every `session-state.json → runtime` if the faction has a trust
    variable
- Do not reference NPCs by name inside faction files. Let the NPC
  reference the faction instead, one-way.

## Common mistakes

- Putting a whole faction's plot in the description. Plot belongs in
  `lore.md` or adventures.
- Referring to factions with `allies` / `enemies` lists that are not
  declared elsewhere. If it is not in `campaign.yaml → factions`,
  it does not exist.
- Making every faction hostile. Most campaigns should have at least
  one `neutral-good` the party can earn trust with.