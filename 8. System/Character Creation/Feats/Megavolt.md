---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Electricity]]", "[[Inventor]]", "[[Manipulate]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You bleed off some electric power from your innovation in the shape of a damaging bolt. Creatures in a @Template[line|distance:20] from your innovation take @Damage[(max(3,floor(@actor.level/2)))d4[electricity]|options:area-damage] damage, with a [[Reflex]] save against your class DC. The electricity damage increases by 1d4 at 8th level and every 2 levels thereafter.

**Unstable Function** You overload and supercharge the voltage even higher. Add the unstable trait to Megavolt. The area increases to a @Template[line|distance:60] and the damage increases from d4s to d12s. If you have the breakthrough innovation class feature, you can choose a 60-foot or @Template[line|distance:90] for the area when you use an unstable Megavolt; if you also have the revolutionary innovation class feature, you can choose a 60-foot, 90-foot, or @Template[line|distance:120].

**Special** If your innovation is a minion, it can take this action rather than you.

**Source:** `= this.source` (`= this.source-type`)
