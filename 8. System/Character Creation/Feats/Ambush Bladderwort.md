---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Composite]]", "[[Impulse]]", "[[Kineticist]]", "[[Plant]]", "[[Primal]]", "[[Water]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You plant the seed of a giant bladderwort in an unoccupied square of ground or water within 30 feet. It lasts for 10 minutes. Using this impulse again ends any previous one. If a creature enters its square, the seed erupts into a voluminous, translucent plant that seals tight around the triggering creature and fills with water. Unless the creature succeeds at a [[Reflex]] save against your class DC, it's [[Immobilized]] within the bladderwort and must hold its breath or begin drowning. The [[Escape]] DC is also your class DC. The plant has AC 10 and 50 Hit Points.

If a creature dies inside it, the plant shrinks down, converting itself and the remains into a watery fruit. A creature can eat this consumable to regain @Damage[((floor((max(4,@actor.level)-4)/4)+1)d8+(floor((max(4,@actor.level)-4)/4)*4+4))[healing]] HP, after which that creature is temporarily immune for 10 minutes. This fruit rots after 1 hour.

**Level (+4)** The bladderwort's HP increase by 25 and the fruit's healing increases by 1d8+4.

**Source:** `= this.source` (`= this.source-type`)
