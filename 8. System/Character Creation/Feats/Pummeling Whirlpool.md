---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Merfolk]]", "[[Primal]]", "[[Water]]"]
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You draw water from the environs, swirling it into a rough torrent around you to punish your foes. Each creature in a @Template[emanation|distance:10] (or @Template[emanation|distance:15]{15 feet} if you're in a body of water) takes @Damage[8d6[bludgeoning]|options:area-damage] damage with a [[Reflex]] save against the higher of your class DC or spell DC. A creature that fails its save is knocked [[Prone]]. At 17th level, the damage increases to 11d6.

**Source:** `= this.source` (`= this.source-type`)
