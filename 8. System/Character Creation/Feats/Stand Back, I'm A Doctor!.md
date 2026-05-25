---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lepidstadt Surgeon|Lepidstadt Surgeon]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Lepidstadt Surgeon Dedication, master in Medicine"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are holding healer's tools, or you are wearing them and have a hand free; a creature with the [[Dying]] condition is in your reach.

You have mastered techniques to aid those at the brink of death, even if they use dangerous Stasian technology. Attempt a Medicine check on the dying creature as you deliver it a powerful shock. The DC is usually a standard-difficulty DC of a level equal to the target. On a success, the creature's dying condition is reduced by 1 (or 2 on a critical success); if this reduces the value of the dying condition to 0, the creature regains @Damage[(2d8+10)[healing]] Hit Points, its wounded condition doesn't increase, and it can Stand as a free action. Each creature except you adjacent to the target takes 8d6 electricity damage ([[Reflex]] save against your class DC or spell DC); instead of attempting this save, a creature can Step as a free action and if they end this movement not adjacent to the target, they take no damage.

**Source:** `= this.source` (`= this.source-type`)
