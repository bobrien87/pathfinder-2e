---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
prerequisites: "ancestors or battle mystery"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You beseech warrior spirits to come forth and aid you. Two ghostly warriors manifest within a @Template[emanation|distance:30] of you and each attempt a Strike against an adjacent enemy, using your spell attack modifier. The warriors' Strikes each deal 4d6 spirit damage and the warriors can flank with one another and with you and your allies. If you are [[Cursebound 2]] when you use The Dead Walk, you instead summon three warriors, and if you are cursebound 3, you instead summon four warriors. The warriors disappear at the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
