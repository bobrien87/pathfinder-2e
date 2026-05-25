---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You are targeted by a ranged attack.

**Requirements** You are adjacent to an enemy and have [[Panache]].

You attempt to deftly swap places with an adjacent enemy to avoid the attack. Choose an adjacent enemy and attempt to [[Reposition]] it. Instead of the normal results of Reposition, use the following.
- **Critical Success** You swap places with the target enemy and the enemy becomes the target of the triggering attack.
- **Success** As critical success, except the target has lesser cover against the triggering attack, and you lose your panache.
- **Failure** You lose your panache.
- **Critical Failure** You become [[Off Guard]] against the triggering attack, and you lose your panache.

**Source:** `= this.source` (`= this.source-type`)
