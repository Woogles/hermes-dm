adventure:
  id: bramble-stacks
  act: 2
  level_range: "5-7"
  objective: |
    Discover why one Bramble record is physically present but not properly remembered.
  major_clues:
    - book never printed
    - shelf sealed
    - troll guard protects a page no one admits to having
  success_condition: identify future information moved into the past
  failure_condition: paradox +1

  skill_challenge:
    - check: Investigation
      dc: 13
      meaning: the missing record exists physically
    - check: History
      dc: 15
      meaning: the record was copied then erased
    - check: Arcana
      dc: 16
      meaning: the page carries a Ring Anchor signature
    - check: Religion
      dc: 16
      meaning: a witness memory was made to be believed
    - check: Persuasion
      dc: 14
      meaning: one guard can be convinced to reveal the page

  beginner_rule: >
    If the party fails two checks but explains what they are trying to learn, let them use a
    Case Mark to get one true detail.


    The real issue is:

    The page exists physically.
    The question is whether it was written in the past or brought from the future.
    If believed as real, it destabilizes history.