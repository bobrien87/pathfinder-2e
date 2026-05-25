---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Lizardfolk]]", "[[Primal]]"]
prerequisites: "bakuwa lizardfolk heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You call on the spirit of the dragon that devoured the moon to temporarily swallow a celestial body and blind onlookers with its visage. You can cast [[Eclipse Burst]] as a primal innate spell once per day. When you Cast the Spell, the sun or moon appears to eclipse to all creatures within 500 feet of you. For 1 round after Casting the Spell, the area is reduced to dim light.

**Source:** `= this.source` (`= this.source-type`)
