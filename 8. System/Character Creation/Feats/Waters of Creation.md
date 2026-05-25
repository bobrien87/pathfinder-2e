---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Healing]]", "[[Oracle]]", "[[Vitality]]", "[[Water]]"]
prerequisites: "life or tempest mystery"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Water is the source of life, and you draw upon this primordial force to heal your allies' wounds. A gentle ring ripples out from you in a @Template[emanation|distance:15], restoring @Damage[(floor(@actor.level/2))d6[healing,vitality]|shortLabel:true] Hit Points to creatures in the area. At 12th level and every two levels thereafter, the amount restored increases by 1d6. If you are [[Cursebound 3]] when you use Waters of Creation, the amount healed increases to @Damage[(floor(@actor.level/2))d8[healing,vitality]|shortLabel:true].

**Source:** `= this.source` (`= this.source-type`)
