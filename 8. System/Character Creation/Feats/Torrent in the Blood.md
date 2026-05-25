---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Healing]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Overflow]]", "[[Primal]]", "[[Vitality]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A healing wave splashes across creatures in a @Template[cone|distance:30], its cleansing water driving afflictions from the body. Each creature in the area regains @Damage[(floor((max(6,@actor.level)-6)/2)+3)d8[healing]] HP and can attempt a new save against one poison or disease affliction affecting it; on a failed save, the condition doesn't worsen.

Each creature that benefited from this impulse becomes temporarily immune to Torrent in the Blood for 10 minutes.

**Level (+2)** The healing increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
