adventure:
  id: silent-century
  act: 2
  level_range: "7-8"
  objective: |
    Stabilize the Ring before it collapses.
  major_clues:
    - ring fracture
    - true anchor sequence
    - founding memory
  success_condition: repair Ring and open Underhollow safely
  failure_condition: major paradox

  skill_challenge:
    - check: Investigation
      dc: 16
      meaning: locate the Ring fracture
    - check: Arcana
      dc: 17
      meaning: find the true anchor sequence
    - check: History
      dc: 18
      meaning: prove the correct founding memory
    - check: Religion
      dc: 18
      meaning: silence or correct a false witness
    - check: Persuasion
      dc: 17
      meaning: gain Silver Council trust

      The final result:

    They repair the Ring.
    They open the Underhollow.
    The Unseen Century is still active.
    The Silver Council becomes a faction.