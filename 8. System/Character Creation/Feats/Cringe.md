---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Emotion]]", "[[Kobold]]", "[[Mental]]", "[[Visual]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature you are aware of critically succeeds on a Strike against you and would deal damage to you.

With pitiful posturing, you cause your foe to pull back a deadly attack. The attacking creature takes a circumstance penalty to the damage of the triggering Strike equal to your level + 2. This penalty applies after doubling the damage for a critical hit. The attacker is then immune to your Cringe for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
