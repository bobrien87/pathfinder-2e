---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spit out a freezing breath or sonic scream. You deal 4d6 damage, plus 1d6 damage for every level you have beyond 6th (@Damage[(-2+@actor.level)d6[untyped]|options:area-damage]), to all creatures in a @Template[cone|distance:30], with a [[Reflex]] save.

**Awakening** Your blast powerfully batters your foes. A creature that critically fails its save is knocked [[Prone]].

**Awakening** The kickback of your blast helps you make a speedy escape. When you use this ability, you Fly backward 15 feet in a straight line directly opposite your blast. This movement doesn't trigger reactions based on movement.

**Source:** `= this.source` (`= this.source-type`)
