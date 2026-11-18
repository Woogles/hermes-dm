adventure:
  id: library-no-exit
  act: 1
  level_range: "1-2"
  objective: |
    Discover why the library remembers a different history.
  major_clues:
    - missing shelf
    - altered plaque
    - witness contradiction
  success_condition: identify source of anomaly
  failure_condition: paradox +1

  skill_challenge:
    - check: Investigation
      dc: 10
      meaning: find the missing shelf space
    - check: History
      dc: 10
      meaning: learn why the plaque feels wrong
    - check: Insight
      dc: 12
      meaning: notice one witness memory is too perfect
    - check: History
      dc: 13
      meaning: reconstruct what happened first

  known_on_success: >
    The plaque changed before the statue was carved. The statue remembers the old name.
    The library remembers the new name.

  known_on_failure_with_plan: >
    You find that the book is not missing. It was never physically removed. It was removed from history.

    Begin the session with investigation. Ask one simple question:

    “What do you investigate first?”
    “What do you ask witnesses?”
    “Do you trust memory, records, or physical proof?”

If a player compares two memories, allow one Case Mark.