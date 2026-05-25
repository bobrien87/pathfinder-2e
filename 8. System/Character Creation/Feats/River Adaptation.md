---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Lizardfolk]]"]
prerequisites: "makari lizardfolk heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Webbing sprouts on your legs and tail as you shift to a more aquatic form. You can cast [[Feet to Fins]] as an innate divine spell once per day. This innate magic relies on your makari heritage, limiting the effect to yourself but allowing you to cast it more easily than a common mage; you can target only yourself with the spell, but you can Cast the Spell as a free action if you're within a body of water when you cast it.

**Source:** `= this.source` (`= this.source-type`)
