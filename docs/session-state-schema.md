# Session-State Schema (v1)

Documents `data/campaigns/<id>/session-state.json`. State is LIVE VALUES
only. Definitions (display_name, type, default) live in
`campaign.yaml runtime_variables`, NOT here. This separation is what
lets you ship `v1.2` without wiping saves.

## File location

`data/campaigns/<campaign-id>/session-state.json` — one per game.

## Shape (authoritative)

    {
      "campaign": "string (id pattern)",
      "schema_version": "integer >= 1",
      "campaign_version": "string (1.0 | 1.2 ...)",
      "created_at": "ISO8601 | empty-string-seed",
      "updated_at": "ISO8601 | empty-string-seed",
      "session_number": "integer >= 0 (0 = starting new)",
      "current_act": "integer >= 1 (0 allowed only on blank seed)",
      "current_adventure": "id pattern",
      "current_location": "id pattern",
      "active_quests": ["id pattern"],
      "quests_completed": ["id pattern"],
      "runtime": { "live runtime values keyed by campaign.yaml id" }
    }

## Field semantics

- `campaign` must equal `campaign.yaml campaign.id`.
- `schema_version` mirrors `campaign.yaml schema_version` for migration.
- `campaign_version` mirrors `campaign.yaml campaign_version` (release
  text fixes) — independent of schema_version.
- `created_at` / `updated_at`: loader writes real ISO stamps on game
  creation. `updated_at` refreshes on save. Blank seed files may carry
  empty strings; the loader fills them on first load.
- `session_number`: 0 when starting a new game. Incremented ONLY when the
  DM advances to a new playable session (Session 0 is the setup).
- `active_quests`: quest ids currently underway. On Session 0 the loader
  seeds `[opening_quest_id, current_adventure]`.
- `quests_completed`: finished quest ids (adventure ids). On resolving an
  adventure: remove from `active_quests`, append to `quests_completed`.
- `runtime`: only the keys defined in `campaign.yaml runtime_variables`.
  A key here with no matching definition = obsolete, dropped by migration.

## Migration rules (authoritative — mirror of schema.yaml)

When loading a game whose `schema_version` is HIGHER than the file's:
1. Load `campaign.yaml` + `campaign.yaml runtime_variables`.
2. Keep every existing runtime value whose id still exists.
3. Apply `default` from `campaign.yaml` for newly added runtime vars.
4. Drop runtime values whose ids are no longer defined.
5. Clamp numeric runtime values to current min/max.
6. For string vars with `allowed:`, drop invalid values → set default.
7. Never touch `created_at`, `session_number`, `active_quests`,
   `quests_completed`, `current_act/adventure/location` during migration.

## Worked example

Saved (v1):
    { "schema_version":1, "campaign_version":"1.0",
      "runtime":{ "case_marks":1, "paradox_track":3 } }

You release v1.2 with new var `witness_trust` and `case_marks default:4`:

After migration:
    { "schema_version":2, "campaign_version":"1.2",
      "runtime":{ "case_marks":1, "paradox_track":3, "witness_trust":50 } }

`case_marks:1` is preserved (not overwritten by 4). `paradox_track:3` clamped
if max shrank. New `witness_trust` added with its default.

## Loader validation order (strict)

1. Validate file against `schema_state.json` (see schema_state.json file).
2. Resolve `campaign.yaml` and its `runtime_variables` + `resources` + `quests`.
3. Migrate if schema_version differs.
4. Check `active_quests`/`quests_completed` ids exist in
   `campaign.yaml quests.quest_ids`.
5. Check `runtime` keys ⊆ `campaign.yaml runtime_variables` keys.
6. Check `current_location`/`current_adventure` ids exist in `resources`.
7. Check numeric clamps; report warnings, never fail outright.

## Common mistakes

- Storing display names or DCs in state — those are definitions, not values.
- Putting lore/session history inside `runtime` — not the place.
- Treating `session_number` like "number of saves". It is play-session index
  (0 = setup).
- Renaming `active_quests`/`quests_completed` keys in a new release without
  bumping `schema_version` — breaks migration.
- Reusing `created_at`/`updated_at` for anything other than real timestamps.

## Cross-reference contract

- `campaign` ⇄ folder ⇄ `campaign.yaml.id`.
- every quest id ⇄ `campaign.yaml quests.quest_ids`.
- every runtime key ⇄ `campaign.yaml runtime_variables`.
- every location/adventure id ⇄ `campaign.yaml resources`.