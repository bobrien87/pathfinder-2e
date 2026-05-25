---
type: action
source-type: "Remaster"
traits: ["[[Stance]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're unarmored and wielding a simple firearm or simple combination weapon

**Effect** You enter a specialized stance for a unique martial art centered around the use of simple firearms. While in this stance, the only Strikes you can make are those using bayonets, reinforced stocks, simple firearms, and simple combination weapons. You can use [[Flurry of Blows]] with these weapons. You can use other monk feats or monk abilities you have that normally require unarmed attacks with bayonets, reinforced stocks, and the melee component of simple combination weapons, so long as the feat or ability doesn't require a single, specific Strike. You can also use them with simple firearms when attacking within half the first range increment.

**Source:** `= this.source` (`= this.source-type`)
