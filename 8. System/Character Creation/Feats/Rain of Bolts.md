---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Automaton]]"]
prerequisites: "Sharpshooter automaton"
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Throughout the day, your body produces powerful projectiles within your chassis. You fire them all at once in either a @Template[type:cone|distance:30] or a @Template[type:emanation|distance:10]. Foes in the area take @Damage[(3 + floor(@actor.level/3))d6[piercing]|options:area-damage] damage with a [[Reflex]] save against the higher of your class DC or spell DC. This increases to 7d6 at 12th level, 8d6 at 15th level, and 9d6 at 18th level.

**Enhancement** The projectiles regenerate quicker, they are much more powerful, and you can refine the metallic content to harm certain creatures. You can use Rain of Bolts once per hour instead of once per day. The damage increases to 12d6 and each time you use the action, you can choose adamantine, cold iron, or silver. The damage from Rain of Bolts is treated as the metal you chose. At 20th level, the damage increases to 13d6.

**Source:** `= this.source` (`= this.source-type`)
