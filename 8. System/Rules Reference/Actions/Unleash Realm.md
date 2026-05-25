---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:0`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your previous action was to Sustain your manifested realm

**Effect** You punish those who transgress upon your realm. An enemy within your realm takes @Damage[4d8[@actor.flags.system.realmDamage]|shortLabel|options:area-damage] damage of your realm's damage type with a [[Fortitude]] save against your class DC or spell DC, whichever is higher.

**Source:** `= this.source` (`= this.source-type`)
