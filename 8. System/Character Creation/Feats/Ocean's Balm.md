---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Healing]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Primal]]", "[[Vitality]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A blessing of the living sea salves wounds and douses flames. Touch a willing living creature. It regains @Damage[(floor((max(1,@actor.level)-1)/2)+1)d8[healing]] HP and gains resistance 2 to fire for 1 minute. If it has persistent fire damage, it can attempt a flat check to remove it with especially appropriate help. The target is temporarily immune to healing from Ocean's Balm for 10 minutes.

**Level (+2)** The healing increases by 1d8, and the resistance increases by 1.

> [!danger] Effect: Ocean's Balm

**Source:** `= this.source` (`= this.source-type`)
