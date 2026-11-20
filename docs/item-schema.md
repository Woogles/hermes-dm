# Item Schema (v1)

## Purpose

Describes one object the party can find, hold, spend, or use. Items are
not loot drops. They are **investigation tools** and **story resources**
the DM can hand out to help a beginner party.

## File location

`campaigns/<campaign-id>/items/<item-id>.yaml`

Filename must equal id. Registered in:
- `campaign.yaml → resources → items`
- usually also `campaign.yaml → resources → rewards`

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | kebab-case unique id |
| `name` | string | display name |
| `rarity` | enum | (see below) |
| `mechanical` | text | what the party can **do** with it, in plain rules |

## Optional fields

| Field | Type | Meaning |
|---|---|---|
| `kind` | string | short tag, e.g. `investigative-tool`, `resource`, `story-item`, `key` |
| `requires_attunement` | boolean | only for permanent artifacts |
| `actions` | list | explicit action blocks |
| `senses` | list | explicit senses or passive detections |
| `repair_pulse` | list | a single per-rest heal-like effect |
| `warning` | text | how the item interacts badly with other rules |
| `narrative` | text 1–2 sentences | flavor, optional |

## Allowed `rarity` values

    common
    uncommon
    rare
    very-rare
    legendary
    artifact
    wondrous
    story

For story-only resources the DM controls, use `story`.
For permanent campaign artifacts use `wondrous` or `artifact`.

## Example (real, from paper-circus)

    item:
      id: archive-lens
      name: Archive Lens
      rarity: uncommon
      kind: investigative-tool
      mechanical: >
        Once per long rest, spend a bonus action to see whether one
        paper record is a true copy, a copied false version, or a
        witness echo.

## Author checklist for a new item

1. Decide the item's job first: **reveal**, **stabilize**, **travel**,
   or **resist**. If none of those, it is not a campaign item.
2. Write `mechanical` in the 5.5e voice the party can act on: "spend a
   bonus action to…". Never write "the DM decides".
3. Set a per-use limit. Items without limits become exploits:
   `once per long rest`, `spend one token`, `once`, `requires
   attunement`.
4. If the item touches runtime variables, name them exactly. Example:
   "spend one `memory_marks`" (matches the runtime key).
5. Do not put item effects in the adventure. The adventure references
   the item by id.

## Cross-references

- Item ids appear in:
  - `campaign.yaml → resources → items`
  - `campaign.yaml → resources → rewards`
  - `campaign.yaml → runtime_variables` (for counts like `tide_keys`,
    `ring_anchor_tokens`)
- Any runtime variable that counts the item should exist in
  `campaign.yaml → runtime_variables` and the item file's `mechanical`
  should use the same key.

## Common mistakes

- Making every item an attack bonus. These items should **reveal
  something the party didn't know**, not boost damage.
- Skipping the per-use limit. That lets a low-level party hoover the
  campaign.
- Writing `mechanical` in prose ("you feel a tingle"). Be explicit.
- Naming an item with capitals: `Archive Lens`. Id must be
  `archive-lens`. Display `name` can have capitals; `id` cannot.