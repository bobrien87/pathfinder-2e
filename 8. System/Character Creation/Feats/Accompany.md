---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Bard]]", "[[Concentrate]]", "[[Manipulate]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally within 30 feet Casts a Spell.

You use your performance to supplement an ally's spellcasting, providing magical energy for their spell in their stead. Attempt a Performance check, using a very high DC for the ally's level, and either spend a Focus Point (if the triggering spell is a focus spell) or expend a spell slot at least 1 rank higher than the triggering spell. If you succeed at your Performance check, your ally's spell doesn't cost the Focus Point or spell slot that ally would normally need to spend.

**Source:** `= this.source` (`= this.source-type`)
