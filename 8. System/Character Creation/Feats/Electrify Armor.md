---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Inventor]]", "[[Manipulate]]"]
prerequisites: "armor innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wearing your armor innovation.

You electrify your armor to punish foes who dare to attack you. For 1 round, any creature that touches you, or that hits you with a melee unarmed attack or a non-reach melee weapon attack, takes @Damage[1d4[electricity]|overrideTraits] damage. The effect ends if you cease wearing your armor innovation.

If you have the revolutionary innovation class feature, the damage increases to 2d4.

**Unstable Function** You create an unstable chain reaction, sending countless sparks dancing across your armor. Add the unstable trait to Electrify Armor. The effects last for 1 minute instead of 1 round, and the damage dice increase from d4s to d12s.

**Source:** `= this.source` (`= this.source-type`)
