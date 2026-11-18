adventure:
  id: missing-rainstorm
  act: 1
  level_range: "1-4"
  objective: |
    Discover why a town remembers a rainstorm that no record shows.
  major_clues:
    - dry riverbed
    - photo of flooded street
    - missing page from yearbook
  success_condition: stabilize the water choice
  failure_condition: paradox +1

  skill_challenge:
    - check: Nature
      dc: 12
      meaning: weather pattern mismatch
    - check: History
      dc: 13
      meaning: public memory vs records
    - check: Investigation
      dc: 12
      meaning: the photo was taken during a real event
    - check: Arcana
      dc: 15
      meaning: a magical echo was left in town memory
    - check: Persuasion
      dc: 14
      meaning: ask a witness if they remember physically or only through stories

  simple_answer: >
    The rain did not disappear naturally. It was moved by a magical echo.

  choices:
    - Save the present water supply.
    - Return water to the past using a safe ring node.
    - Stabilize the memory only.

    The DM should make the choice easy to follow:

    Solve the practical problem.
    Solve the mystery.
    Keep history stable.