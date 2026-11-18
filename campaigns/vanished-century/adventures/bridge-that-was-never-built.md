adventure:
  id: bridge-that-was-never-built
  act: 2
  level_range: "5-6"
  objective: |
    Discover why a bridge exists in memory but not in city maps.
  major_clues:
    - child remembers walking across it
    - bus driver remembers avoiding it
    - physical street is broken in two places
  success_condition: prove the bridge anchor
  failure_condition: paradox +1

  skill_challenge:
    - check: Investigation
      dc: 13
      meaning: there is a real gap where the bridge stood
    - check: Nature
      dc: 14
      meaning: road wear matches old traffic, not modern construction
    - check: History
      dc: 15
      meaning: a bridge was removed from official memory during one decade
    - check: Arcana
      dc: 16
      meaning: a ley-line node is under the broken gap

  ring_entry_rule:
    - follow a known anchor: 1 Case Mark, safe
    - use a witness memory: 2 Case Marks, safe but witness changes
    - follow a stolen item: automatic paradox, risky

    Encounter note:

    The party should ask: Are they guards? Are they witnesses? Are they enemies?

Options:

    Talk to the Silent Auditor.
    Prove they are witnesses.
    Fight only if provoked.
    Find a safer entry.