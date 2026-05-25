---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Orc]]"]
prerequisites: "animal companion, Pet, or Bonded Animal, Orc Ferocity"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Since ancient times, the mightiest orc beast tamers would draw out the true fighting spirit of their companion beasts by feeding the creatures a draft incorporating the orc's own blood. All animal companions, pets, familiars, and bonded animals you have gain the [[Orc Ferocity]] feat, and gain one reaction per round they can use only for Orc Ferocity. If you have the [[Undying Ferocity]] ancestry feat, all animal companions, pets, familiars, and bonded animals you have also gain the benefits of that feat when using the Orc Ferocity reaction.

**Source:** `= this.source` (`= this.source-type`)
