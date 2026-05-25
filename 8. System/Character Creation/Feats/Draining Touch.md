---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Cold]]", "[[Deviant]]", "[[Magical]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You reach out your arm, grasping hungrily for a source of energy. Attempt a melee Strike. If you succeed, you deal 1d8 cold damage for every 2 levels you have to the target (@Damage[(floor(@actor.level/2))d8[cold]]), or double damage on a critical success.

**Awakening** You drain enough energy from a creature to leave it with lingering aftereffects. Your Draining Touch also leaves a creature [[Clumsy]] 1, or [[Clumsy]] 2 if your attack was a critical success.

**Awakening** You can pull away not just physical energy, but a creature's spirit as well. Your Draining Touch can deal your choice of cold, spirit, or void damage, changing the cold trait to spirit or void as appropriate.

**Source:** `= this.source` (`= this.source-type`)
