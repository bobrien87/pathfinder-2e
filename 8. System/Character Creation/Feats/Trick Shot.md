---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded crossbow or firearm.

You shoot not at your foe but at an object nearby. Make a Strike with your firearm against an AC equal to an easy DC for your level. On a success, instead of hitting your foe, your attack hits an object behind or to the side of your target, creating one of the following effects. The GM might determine that a different AC is appropriate or that a particular effect isn't a valid option, such as using the explosive barrel option when there's no such object on the battlefield. The GM should inform you if a Trick Shot is feasible before you spend your actions, since your trained eye can easily recognize loose or volatile objects.

- **Dislodge Object** Your attack knocks an unattended object of no more than 2 Bulk out of position, moving it up to 10 feet in a direction of your choice. For example, the weapon could knock a wizard's crystal ball off a table.
- **Explosive Barrel** Your attack strikes a barrel of expensive rum, a vial of volatile alchemical fluids, a demonic pustule erupting from the earth, or some other explosive object. The object explodes in a @Template[type:burst|distance:20], and creatures in the area take @Damage[(6 + floor((@actor.level - 10) / 2))d6|options:area-damage] damage with a [[Reflex]] save against your class DC. The damage type is chosen by the GM, based on the exploding object. Increase the damage by 1d6 for every 2 levels you have above 10th.

**Source:** `= this.source` (`= this.source-type`)
