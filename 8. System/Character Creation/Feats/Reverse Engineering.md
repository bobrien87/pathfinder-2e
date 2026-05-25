---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scrounger|Scrounger]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "expert in Crafting, Scrounger Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your nigh-constant tinkering and fiddling with objects means you are able to reverse engineer items into formulas more effectively than most.

You gain a +2 circumstance bonus to Crafting checks to reverse engineer a formula from an item, and you can attempt a Crafting check to reverse engineer an item after spending 1 day of work setting up instead of 2. Additionally, if you get a critical success on your Crafting check, you can opt to not only create the formula but also reassemble the original item at the same time, leaving you with the formula and the item instead of the formula and raw materials equal to half the item's value.

**Source:** `= this.source` (`= this.source-type`)
