---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fire]]", "[[Inventor]]", "[[Manipulate]]", "[[Sonic]]", "[[Visual]]"]
prerequisites: "weapon innovation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

Your weapon contains a detonation chamber that launches fireworks, sparklers, and black powder pellets that sizzle, twist, and scatter on the ground in a cacophonous manner liable to annoy the entire Celestial Court. All creatures in a @Template[type:cone|distance:15] extending from your innovation take @Damage[(max(3,(floor(@actor.level / 2) - 3)))d4[fire],(max(3,(floor(@actor.level / 2) - 3)))d4[sonic]|options:area-damage] damage with a [[Fortitude]] save against your class DC; both the fire and sonic damage increase by 1d4 at 14th level and every 2 levels thereafter. The area affected by the cone becomes difficult terrain until the start of your next turn. Creatures moving through this area must succeed at a [[Reflex]] save against your class DC or take 2d4 persistent,fire damage.

**Unstable Function** You rattle your weapon violently to make it belch out even more pyrotechnics. Add the unstable trait to Celestial Cacophony. The area increases to a @Template[type:cone|distance:30], and all damage dice increase from d4s to d8s.

**Source:** `= this.source` (`= this.source-type`)
