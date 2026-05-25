---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Arcane]]", "[[Thaumaturge]]"]
prerequisites: "Thaumaturge's Demesne"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can move your demesne here and there, bringing it wherever your journey takes you. Your demesne expands to a maximum of 10,000 square feet. Once per day, you can call your demesne forth, which takes 1 minute. This has the effects of [[Resplendent Mansion]], except that it conjures your demesne from its previous location, with all the benefits of Thaumaturge's Demesne in addition to the those of the spell. You must be able to claim the new area, with the same restrictions as Thaumaturge's Demesne.

**Source:** `= this.source` (`= this.source-type`)
