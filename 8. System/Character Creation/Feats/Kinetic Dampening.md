---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You feed off energy in your immediate surroundings, allowing you to dampen the force imparted by incoming blows. Until the beginning of your next turn, you gain resistance 5 to physical damage. At 10th level, and every 4 levels thereafter, the resistance increases by 5. Any blows that strike you during this time make no sound as their energy is drained.

**Awakening** You can extend your dampening field around you to create a safe haven for your allies. If you spend an additional action when using Kinetic Dampening, your field extends in a @Template[type:emanation|distance:15] around you. You can choose which creatures within the emanation are affected.

**Awakening** You dampen a greater variety of wavelengths. When you use this feat, you also gain resistance to your choice of fire, electricity, or sonic damage.

**Source:** `= this.source` (`= this.source-type`)
