---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Barbarian]]", "[[Rage]]"]
prerequisites: "Collateral Thrash"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You whirl a foe to smash into all nearby creatures before throwing them far away. You [[Thrash]]. During this Thrash, your [[Collateral Thrash]] feat applies to all other enemies adjacent to you. You can then throw the [[Grabbed]] creature 10 feet, where they fall [[Prone]].

If the enemy you choose for Collateral Thrash is also adjacent to you, it attempts only one save and takes the damage only once.

**Source:** `= this.source` (`= this.source-type`)
