---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Crossbow Infiltrator|Crossbow Infiltrator]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Stealth"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have mastered stealthy weapons that allow you to strike carefully from a distance far enough to avoid reprisal, yet close enough to confirm your kills. You have familiarity with the [[Gauntlet Bow]], [[Hand Crossbow]], and [[Repeating Hand Crossbow]], treating the repeating hand crossbow as a martial weapon for the purposes of proficiency and the gauntlet bow as a simple weapon for the purposes of proficiency. If you're at least an expert in any of these weapons, you gain access to that weapon's critical specialization effect. You also gain the [[Infiltrator's Draw]] action.

Crossbow Infiltrator

**Source:** `= this.source` (`= this.source-type`)
