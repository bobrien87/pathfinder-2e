---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Commander]]", "[[Mental]]"]
prerequisites: "Deceptive Tactics"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You shout out bewildering but authoritative commands while imitating the voices, linguistic quirks, and speech patterns of your opponents. Each enemy within the aura of your commander's banner must succeed at a [[Will]] save against your class DC or become [[Confused]] for 1 round (2 rounds on a critical failure).

Targets who succeed at their saving throw are temporarily immune to Confusing Commands for 1 day.

**Source:** `= this.source` (`= this.source-type`)
