---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Automaton]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your body is designed to be particularly resilient. Your chassis is made from reinforced armor plating that grants a +3 item bonus to AC with a Dexterity cap of +1. If you are at least 5th level, the item bonus increases to +4 and at 10th level it increases to +5. You can never wear other armor or remove your chassis; however, you still don't become [[Fatigued]] from sleeping. You can etch armor runes onto your chassis. Your chassis is medium armor in the plate group for abilities and for etching runes.

**Enhancement** Your chassis becomes difficult to overcome. You gain the [[Chassis Deflection]] reaction.

**Source:** `= this.source` (`= this.source-type`)
