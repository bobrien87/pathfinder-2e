---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Stone encases you like armor. The stone armor is medium armor but uses your highest armor proficiency. The stone armor's statistics are: AC Bonus +4; Dex Cap +1; Check Penalty –2; Speed Penalty –10 feet; Strength +3; Bulk 1; Group plate. You gain its armor specialization effect. Any bonuses, runes, and magical abilities of your actual armor are suppressed, but any runes that could apply to the stone armor are replicated onto it. The stone armor lasts for 10 minutes, and you can Dismiss this impulse. If you use this impulse again, any existing one ends.

**Level (3rd)** The armor becomes heavy armor. Its AC Bonus becomes +5, and it gains the bulwark armor trait.

**Source:** `= this.source` (`= this.source-type`)
