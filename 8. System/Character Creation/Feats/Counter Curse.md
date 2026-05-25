---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Curse Maelstrom|Curse Maelstrom]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Curse Maelstrom Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You or an ally within 30 feet is targeted by or in the emanation of a curse or misfortune effect from an opponent or object of which you're aware.

**Requirements** You're in a curse maelstrom state.

You gather the energy of your maelstrom and fling its unleashed power into the enemy's curse, attempting to neutralize it. Attempt a counteract check against the triggering effect, using half your level rounded up as your counteract rank and the higher of your class DC – 10 or spell DC – 10 as the counteract modifier. On a success, you neutralize the curse or misfortune effect. If the effect was constant, such as a misfortune aura, it returns automatically at the beginning of the creature or object's next turn. Whether you succeed or fail, your curse maelstrom state ends.

**Source:** `= this.source` (`= this.source-type`)
