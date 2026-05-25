---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Monk]]"]
prerequisites: "Kaiju Stance"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Kaiju Stance]] and are touching the ground.

You slam the ground and unleash a fearsome roar, sending broken shards of earth flying in all directions. The ground in a @Template[type:emanation|distance:20] around you becomes difficult terrain, or greater difficult terrain if it was already difficult terrain. All other creatures within the emanation take @Damage[7d6[bludgeoning]|options:area-damage] damage with a [[Reflex]] save against your class DC. You then can't use World-breaking Footfall for `r 1d4 #Recharge World-Breaking Footfall`.

**Source:** `= this.source` (`= this.source-type`)
