# New campaign template

Fork this folder into `campaigns/<your-id>/`, replace `template-campaign`
and every `CHANGE-`/`TBD` marker, fill enums from `schema.yaml`, then load.
Author-facing rules: `campaign-schema.md`, `lore-schema.md`,
`rewards-schema.md`, `session-state-schema.md`, and the six unit docs
(`npc/location/adventure/encounter/faction/item-schema.md`).

Fork ritual (FORK-CHECKLIST.md):
1. copy folder, rename `template-campaign` -> your kebab-case id everywhere
   (folder, campaign.yaml id, state seed, docs, resource ids).
2. pick difficulty + status + style + recommended_players (enums).
3. fill description (<=60 words) + theme + author.
4. write lore: summary block + mandated H2 prose.
5. declare EVERY runtime variable before using it in ai_instructions,
   items, rewards, or acts.
6. build factions/locations/npcs/adventures/encounters/items as small
   .yaml files; ids = filenames; kebab-case.
7. fill `resources` and `quests` (quest_id = adventure_id).
8. author `dm_behavior.yaml` (its own file, NEVER inside campaign.yaml).
9. write session0.md.
10. create the blank state seed in data/campaigns/<id>/session-state.json
   (created_at/updated_at stay "" — loader fills on first load).