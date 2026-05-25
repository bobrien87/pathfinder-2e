---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonblood]]", "[[Lineage]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your blood surges with the might of dragons who master the waters, and you can move freely in their domain. You gain a swim Speed of 15 feet; if you already have a base swim Speed, it increases by 5 feet. You can hold your breath underwater for 10 minutes before needing air, and you take only a –1 circumstance melee penalty to slashing or bludgeoning attacks that pass through water (instead of –2). If you choose a draconic exemplar, you must choose a dragon with a swim Speed.

**Source:** `= this.source` (`= this.source-type`)
