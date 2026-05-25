---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fighter]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An opponent casting a spell that targets you critically fails a spell attack roll against your AC.

**Requirements** You have a shield raised.

You reflect the spell back against its caster. Make a ranged attack against the attacker using your highest proficiency with a ranged weapon. If you can cast spells, you can choose to make a spell attack roll instead. If you succeed, your opponent takes the effects of a successful spell attack roll for their own spell (or the effects of a critical success if your attack roll was a critical success).

**Source:** `= this.source` (`= this.source-type`)
