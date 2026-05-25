---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Small pieces of metal fly from you, propelled with magnetism at great velocity. Make ranged Impulse check{impulse attack} rolls against up to three creatures within 60 feet of you; you gain a +1 circumstance bonus to your attack roll against any target wearing metal armor or made of metal. All three attacks count toward your multiple attack penalty, but it doesn't increase until after all the attacks. The metal pieces deal @Damage[(floor((@actor.level -1)/2)+1)d4[bludgeoning],(floor((@actor.level -1)/2)+1)d4[piercing]] damage on a hit (or double damage on a critical hit).

**Level (+2)** Each type of damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
