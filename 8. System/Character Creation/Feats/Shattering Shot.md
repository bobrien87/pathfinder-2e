---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm or loaded crossbow and are wearing or holding an alchemical bomb.

You fling a bomb into the air and then shoot it with your gun before it falls, raining destruction down over a wide area. If necessary, you Interact to draw the bomb and regrip your weapon. You throw your bomb to the corner of a square within your firearm's first range increment and shoot it with your firearm. All creatures in a @Template[type:burst|distance:15] of the bomb take the bomb's normal damage with a [[Reflex]] save against your class DC. They don't take any splash or persistent damage the bomb would deal normally.

**Source:** `= this.source` (`= this.source-type`)
