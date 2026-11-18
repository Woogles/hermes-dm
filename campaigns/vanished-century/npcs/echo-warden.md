npc:
  id: echo-warden
  name: Echo Warden
  faction: unseen-century
  importance: major
  disposition: cautious
  secrets: 3
  first_appearance: library-no-exit

  role: >
    Confuses witnesses and tests whether they remember the same event.

  behavior:
    - uses reactions to confuse witnesses
    - creates one fake echo
    - cannot fight for too long

  lesson: >
    Use Insight or Arcana before attacking.

  insight_on_success: >
    You realize the Echo Warden is not attacking people. It is testing whether witnesses
    remember the same event.

  arcana_on_success: >
    You find that its magic leaves tiny frost marks on old records.