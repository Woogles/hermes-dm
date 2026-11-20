# Lore Schema (v1)

Defines the shape of `lore.md`. Markdown is for narrative prose, BUT this
file is no longer free-form: it carries one machine-readable summary block
plus mandated prose sections. The block lets the AI DM load truth without
parsing prose.

## File location

`campaigns/<campaign-id>/lore.md` (exactly one per campaign)

## Required structure (top to bottom)

1. H1 title: `# <Campaign Title> Lore`
2. A fenced block tagged `lore:` containing machine-readable summary:
   - `premise:` one paragraph (≤120 words) — what the party is doing.
   - `world_layers:` list of {id, name, kind, description} — where the
     party can be. kind from location-schema (town/underhollow/hidden-network/etc).
   - `core_rule:` one paragraph — the truth-model (e.g. physical vs memory).
   - `party_role:` list — who the party is / what they value.
   - `skill_dc_tiers:` optional map (beginner/intermediate/advanced → DC ranges).
3. Prose sections, each under an H2 (mandated):
   - `## World layers`
   - `## Core rule`
   - `## Campaign rule` (optional, recommended)
   - `## Paradox handling` (optional, recommended)
   - `## Beginner mistakes to avoid` (required if difficulty: beginner)
   - `## Common mistakes` (required if not beginner — DM self-discipline list)

## Optional sections
   - `## The party's role`
   - `## Eras` (time-travel campaigns)
   - `## Anchors`
   - `## Resources`

## Allowed values
   - world_layers.kind = same enum as location-schema `kind`.
   - difficulty tiers must match `campaign.yaml recommended_players`.
   - skill_dc_tiers values: 10–13 beginner, 12–17 intermediate, 15–23 advanced.

## Example (salt-tide-archive)

    # Salt-Tide Archive Lore

    ```lore:
    premise: >
      A coastal town remembers a flood its records, witnesses and pavement
      disagree about.
    world_layers:
      - {id: salt-tide-archive, name: Salt-Tide Archive, kind: archive, description: >
         tides, floods, harbor names, memories.}
      - {id: harbor-clock, name: Harbor Clock, kind: anchor, description: stable tide anchor}
    core_rule: >
      Physical water evidence is real; memory can be true, false, copied,
      drowned, or made to be believed.
    party_role:
      - investigators
      - keepers of physical evidence
    skill_dc_tiers: { beginner: "10-13" }
    ```

    ## World layers
    ...

    ## Core rule
    Physical marks prove a flood. Memory does not.

    ## Beginner mistakes to avoid
    - do not let memory alone solve the mystery
    - do not hide the one obvious water clue

## Author checklist for a new lore.md

1. Write the `premise:` block BEFORE prose so the DM self-explains.
2. Declare every place the party can visit in `world_layers` (kind from
   location enum) — this is not a place-list, just a map for the DM.
3. State the `core_rule:` in one paragraph: what is truth, what is rumor.
4. If difficulty is beginner, include a "Beginner mistakes to avoid" H2.
5. Keep prose under ~600 words; details belong in adventures.

## Cross-references

- Every `world_layers.id` should match a file in
  `campaigns/<id>/locations/`. Dangling is a soft warning.
- `campaign.yaml theme` tags and `lore:world_layers` must not contradict.

## Common mistakes

- Free-form lore with no summary block → AI DM cannot trust its tone.
- Putting the whole campaign plot in `lore.md`. Lore = world, not story.
- Declaring a world-layer that is also a paradox boss location with no
  location file → soft error "dangling id".
- Writing DCs in lore that contradict `campaign.yaml level_range`.