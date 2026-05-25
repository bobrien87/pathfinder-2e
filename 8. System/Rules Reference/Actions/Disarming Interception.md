---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You have your fist positioned to parry

**Trigger** An enemy within your reach targets you or an ally with a weapon Strike

**Effect** You attempt to [[Disarm]] the weapon the enemy is attacking with. You gain a +2 status bonus to this Disarm check, and if the check is successful, the triggering attack is disrupted. If the Disarm attempt is a critical success and you have a hand free, you can catch the disarmed weapon in your hand instead of it falling to the ground in the target's space.

**Source:** `= this.source` (`= this.source-type`)
