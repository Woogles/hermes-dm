# Fork checklist

- [ ] folder id == campaign.yaml campaign.id == all resource ids == kebab-case
- [ ] difficulty in {beginner, intermediate, advanced}
- [ ] status in {draft, beta, released, deprecated} (skeleton = draft)
- [ ] style.combat/roleplay/exploration each in {low, medium, high}
- [ ] ai_instructions always: has 1 obvious clue + failure reveals; never: block progression (beginner)
- [ ] beginner => style.combat low; never combat_lethality realistic
- [ ] lore has `lore:` fenced block + World layers / Core rule H2s
- [ ] beginner lore has "Beginner mistakes to avoid"
- [ ] every runtime var: display_name, type, default, visible_to_players, scope
- [ ] every resource id has a file; loader "dangling id" must be clean
- [ ] quests: quest_id_equals_adventure_id true + opening_quest_id + quest_ids
- [ ] dm_behavior.yaml separate file: clue_style/mystery_complexity/combat_lethality/
      guidance_level/hidden_information/fail_forward valid enums; booleans present
- [ ] exactly one act lists each adventure id
- [ ] npc.faction and encounter npc refs exist in resources
- [ ] rewards ids exist in items/ AND resources.items; token spend has runtime var
- [ ] state seed: session_number 0, created_at/updated_at "", runtime ""