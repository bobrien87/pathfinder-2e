---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Auditory]]", "[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You release a terrible wail that tears at the spirits of all nearby. All living creatures in a @Template[emanation|distance:20] take @Damage[((@actor.level - 2)d6)[void]|options:area-damage] damage with a [[Fortitude]] save. The damage is 4d6, plus 1d6 for every level you have beyond 6th.

**Awakening** Your scream echoes in the mind. You can choose to emit a silent psychic wail instead, which changes the damage type to @Damage[(@actor.level - 2)d6[mental]|options:area-damage], changes the save to a [[Will]] save, removes the auditory trait, and adds the mental trait.

**Awakening** Your wail saps your foes' strength. In addition to the normal effects, living creatures in the area are [[Enfeebled]] 1 for 1 round on a success (but not a critical success), enfeebled 1 for 1 minute on a failure, and [[Enfeebled]] 2 for 1 minute on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
