# Location Schema (v1)

## Purpose

Describes a single place in the campaign world. Every distinct site is
one YAML file. Locations are the anchors of the campaign — they are where
the party physically goes and what they physically see.

## File location

`campaigns/<campaign-id>/locations/<location-id>.yaml`

Filename must equal id.

## Required fields

| Field | Type | Meaning |
|---|---|---|
| `id` | string | kebab-case unique id |
| `name` | string | display name the DM reads aloud |
| `kind` | enum | what kind of place this is (see enum below) |
| `description` | text 1–2 sentences | what the place looks and feels like |

## Optional fields

| Field | Type | Meaning |
|---|---|---|
| `anchor` | boolean or id | `true` = this location is itself an anchor; an id = this location points at another anchor |
| `tags` | list of strings | extra classification the DM can use |
| `connected_to` | list of ids | other locations you can walk to |
| `public_visible` | boolean | whether ordinary people in the town notice it |

## Allowed values for `kind`

    town hub street public-area public-building
    archive market memory-site anchor paradox-zone
    hidden-network underhollow black-market future-site
    site underground natural-site final-site

Use `anchor` (or `final-site` + `anchor: true`) whenever a place is
**the place the party proves a fact about**. If a location is not an
anchor, do not set `anchor: true`.

## Example (real, from vanished-century)

    location:
      id: library-no-exit
      name: The Library With No Exit
      kind: public-building
      description: >
        A public library whose reading room doors do not match outside.
        A shelf remembers a book that no longer exists physically. A
        statue remembers a different name from its plaque.
      anchor: library-anchor

## Author checklist for a new location

1. Pick an id that the party can use as a **destination**, not as a
   concept. `old-museum-quarter` is a place; `mystery` is not.
2. Choose `kind` before writing the description. Kind decides tone.
3. If this is where the party proves a fact about the anomaly, set
   `anchor: true` (or `anchor: <existing-anchor-id>`).
4. Keep description under 2 sentences. Details belong in the adventure
   file, not the location file.
5. If this place is reachable, list the places you can walk to in
   `connected_to`.

## Cross-references

- The location id appears in:
  - `campaign.yaml → resources → locations: [<id>]`
  - `acts/*.yaml → main_locations`
  - `session-state.json → current_location`
- `anchor: <other-id>` must point at a location that itself is an anchor
  (`kind: anchor` or `anchor: true`).

## Common mistakes

- Describing the whole campaign in one location file. Locations are
  **places**, not plots.
- Forgetting to mark an anchor location as an anchor. Paradoxes will
  break when you need to travel to it.
- Using kind = `mystery`. That is a theme, not a kind.