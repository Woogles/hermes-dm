# Campaign Schema (v1)

Documents the whole `campaign.yaml`. This is the master Layer-1 file: it
defines the campaign AND the variables AND the manifest. It never stores
player progress (that is `session-state.json`).

## File location

`campaigns/<campaign-id>/campaign.yaml`

The `campaign.id` inside the file MUST equal the folder id and the
filename. Example: folder `paper-circus/` → `campaign.yaml` with
`campaign: id: paper-circus`.

## Top-level blocks (order recommended, not required)

1. version
2. campaign (id, title, description, schema_version)
3. author
4. difficulty, status
5. player_count
6. level_range
7. theme
8. style
9. estimated_sessions
10. campaign_type, ruleset, recommended_players
11. ai_instructions
12. runtime_variables
13. resources
14. quests

## Block-by-block reference

### `version`
- integer `1`. Schema line, not campaign line.

### `campaign:`
- `id` — required, kebab-case, == folder == filename.
- `title` — required, display title.
- `description` — required, ≤60 words, one paragraph telling the DM "what
  is this campaign." This is the header the AI reads first.
- `schema_version` — required integer. Bump ONLY when runtime_variables
  changed shape. Used by migration. (Bump `campaign.yaml content` via the
  release version, not this field — see below.)

### `author`
- string, free-form name.

### `difficulty`
enum: `beginner` | `intermediate` | `advanced`

### `status`
enum: `draft` | `beta` | `released` | `deprecated`
- `draft`: skeleton, not playable.
- `beta`: authored, not playtested; ship with state seed.
- `released`: live, playtested.
- `deprecated`: kept for save-compat, not for new games.

### `player_count`
- `min` / `max` integers (typical 3–5).

### `level_range`
- `start` / `end` integers 1–12. Must cover every
  `level_range` string in adventures (e.g. `"1-2"`).

### `theme`
- list of short tags (mystery, investigation, time-anomalies, harbor...).

### `style`
- `combat` / `roleplay` / `exploration`, each enum: `low` | `medium` | `high`.

### `estimated_sessions`
- integer (rough target, not a hard cap).

### `campaign_type` / `ruleset` / `recommended_players`
- `campaign_type`: `story` (v1). `ruleset`: `dnd-5.5e`.
- `recommended_players` enum: `beginner` | `intermediate` | `advanced`.
- Usually `recommended_players == difficulty`. If they differ, difficulty
  wins.

### `ai_instructions:`
Four list blocks, each list of short imperative phrases. The DM reads this
as a behavior contract.

- `emphasize:` what the session leans on.
- `avoid:` what the session must not do.
- `always:` hard guarantees (≥1 obvious clue, one question at a time...).
- `never:` hard bans (never block progression, never hide all clues...).

Beginner campaigns MUST include in `always:` a "one obvious clue" line and
a "failed checks still reveal something" line, and in `never:` a "do not
block progression" line. Beginner `style.combat` = `low`. Beginner never
sets `combat_lethality: realistic`.

### `runtime_variables:`
Declares every DYNAMIC value the campaign uses. Values live in
`session-state.json/runtime`. This file only *defines* them, so you can
release `v1.2` with renamed/added/removed variables without destroying
saves.

Per-variable required metadata (enforced by `schema.yaml`):
- `display_name` (quoted), `type`, `default`, `visible_to_players`.

Per-variable optional metadata:
- `description`, `min`, `max`, `allowed` (list for string enums),
  `scope`, `hidden_reason`.

Allowed `type`: `integer` | `string` | `boolean` | `array` | `object`.
Allowed `scope`: `persistent` (persists) | `session` (reset per session) |
`long_rest` (refill/reset on rest).
Allowed `visible_to_players`: `true` (DM can show plainly) | `false`
(DM-only pressure; do not reveal the number).

Conventions per campaign:
- every resource-like count (Case Marks, Loom Charges, Memory Marks, keys,
  tokens) must be its own variable with `scope` set and `visible_to_players: true`.
- every paradox/danger pressure must be its own integer variable
  (`paradox_track`) with min/max and `visible_to_players: true` for the
  player-facing one; hidden pressure (faction influence) uses
  `visible_to_players: false`.
- any item that spends a token (Bell Token, Ring Anchor Token...) must have
  a matching integer runtime variable.

### `resources:`
A manifest of ids this campaign owns. Keys (v1):
`session, acts, factions, locations, adventures, npcs, encounters, items,
rewards`. Every id listed must have a real file or the loader errors
"dangling id: <id>". This is the auto-load map for a session.

### `quests:`
- `quest_id_equals_adventure_id: true` (the v1 rule).
- `opening_quest_id:` — required, seeds `active_quests` at Session 0
  together with the `current_adventure`.
- `quest_ids:` — list; must contain the opening id + every adventure id +
  the ending id. These are what move from `active_quests` to
  `quests_completed`.

## Required cross-file consistency (loader checks)

- `campaign.yaml` folder id == `campaign.id`.
- every `resources.*` id resolves to a file in that folder.
- every `quests.quest_ids` has an adventure file (except the pure
  opening/ending umbrella ids, which may be `lore`-only if declared as
  quest-only; mark those in their adventure file with `narrative_quest: true`
  or omit them if unused — loader tolerates umbrella ids, errors on typo'd
  adventure ids).
- every `npc.faction` id is in `resources.factions`.
- every `encounter` npc reference is in `resources.npcs`.
- `level_range.start..end` covers all adventure `level_range` strings.
- exactly one `acts/*.yaml` lists each adventure id.

## Example skeleton (paper-circus)

    version: 1.0

    campaign:
      id: paper-circus
      title: The Paper Circus
      description: >
        A beginner memory-mystery campaign where a town remembers a big
        circus parade the ledger, posters and tickets disagree about.
      schema_version: 1

    author: Eric
    difficulty: beginner
    status: released

    player_count: { min: 3, max: 5 }
    level_range: { start: 1, end: 8 }
    theme: [mystery, memory, circus, folklore]
    style: { combat: low, roleplay: high, exploration: medium }

    estimated_sessions: 18
    campaign_type: story
    ruleset: dnd-5.5e
    recommended_players: beginner

    ai_instructions:
      emphasize: [investigation, memory, clues, tickets, posters]
      avoid: [excessive combat, hidden information overload, complex time magic, instant death]
      always:
        - provide at least one obvious clue
        - ask one question at a time
        - let failure reveal something useful
      never:
        - completely block progression

    runtime_variables:
      memory_marks:
        display_name: "Memory Marks"
        type: integer
        default: 3
        min: 0
        max: 5
        visible_to_players: true
        scope: session
      paradox_track:
        display_name: "Paradox Track"
        type: integer
        default: 0
        min: 0
        max: 5
        visible_to_players: true
        scope: persistent

    resources:
      session: [session0]
      acts: [act1, act2, act3]
      factions: [vellam-town-council, forgotten-faces, paper-ticket-ledger, lantern-foxes]
      locations: [grand-pavilion, paper-street, archive-barn, ticket-yard]
      adventures: [missing-ringmaster, phantom-parade, ticket-that-says-nothing, forgotten-circus, archive-of-two-shows, paper-fairground]
      npcs: [ringmaster-quill, missing-girl, ledger-auditor, lantern-fox]
      encounters: [paper-auditor, memory-float]
      items: [memory-ticket, ringmaster-whistle, archive-lens, fairground-compass]
      rewards: [memory-ticket, ringmaster-whistle, archive-lens, fairground-compass]

    quests:
      quest_id_equals_adventure_id: true
      opening_quest_id: the-forgotten-circus
      quest_ids:
        - the-forgotten-circus
        - missing-ringmaster
        - phantom-parade
        - ticket-that-says-nothing
        - forgotten-circus
        - archive-of-two-shows
        - paper-fairground

## Author checklist for a new campaign.yaml

1. Fill `description` first (≤60 words) so the DM can self-explain.
2. Lock enums: difficulty, status, style.*, recommended_players.
3. Declare EVERY runtime variable before referencing it in
   `ai_instructions`, `dm_behavior` examples, or items.
4. Make the beginner contract hard: `style.combat: low`,
   `always:` has the "one obvious clue" + "failure reveals" lines.
5. Fill `resources` completely and confirm every id has a file.
6. Fill `quests` with `quest_id_equals_adventure_id: true` + opening id.
7. Do NOT put `dm_behavior` inside `campaign.yaml` — it is a SEPARATE
   Layer-2 file (see below).

## Common mistakes

- Putting `dm_behavior:` inside `campaign.yaml`. It must be its own file.
- Reusing `schema_version` as the release number. Bump `campaign_version`
  ("1.0"→"1.2") for text fixes; bump `schema_version` ONLY for runtime shape
  changes.
- Defining a runtime variable but listing it nowhere — it becomes dead.
- `status: released` for a campaign that has no `lore.md` or session0.
- Beginner campaign with `style.combat: high`.
- A `resources` id with no matching file → loader fails on load.

## Cross-reference contract

- `campaign.id` ↔ folder ↔ `campaign.yaml campaign.id`.
- `ai_instructions`, `resources`, `quests`, `runtime_variables` are read
  ONLY from this file.
- `dm_behavior.yaml` sits beside it (Layer 2) and never inside it.
- Progress never lives here — it is `data/campaigns/<id>/session-state.json`.