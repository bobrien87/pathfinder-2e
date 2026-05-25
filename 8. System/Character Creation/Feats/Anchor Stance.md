---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Undersea Privateer|Undersea Privateer]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Undersea Privateer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in or under water.

You tense your muscles to make yourself neutrally buoyant and more difficult to move. You gain a +2 circumstance bonus to your Fortitude or Reflex DC against attempts to `act reposition` or `act shove` you. This bonus also applies to saving throws against spells or effects that attempt to force you to move. If any effect would force you to move 10 feet or more, attempt a DC 11 flat check. On a success, you move only 5 feet. Additionally, you don't have to take a Swim action each turn to avoid sinking or moving with the current.

**Source:** `= this.source` (`= this.source-type`)
