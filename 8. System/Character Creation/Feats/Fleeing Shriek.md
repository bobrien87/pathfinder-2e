---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Kobold]]", "[[Sonic]]"]
frequency: "once per PT1H"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You let out an ear-piercing screech. Each creature in a @Template[emanation|distance:10] takes @Damage[ceil(@actor.level/2)d6[sonic]|options:area-damage] damage, with a [[Fortitude]] save saving throw against the higher of your class DC or spell DC. You then Stride, and this movement doesn't trigger reactions from any creature that failed or critically failed its saving throw.

At 11th level and every 2 levels thereafter, the damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
