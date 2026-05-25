---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fortune]]", "[[Occult]]", "[[Psychic]]"]
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A spell you cast has no effect because you critically failed all your spell attack rolls or because all targets critically succeeded at their saving throws.

You see your spell fail to take hold to disastrous end, then snap back to reality—it was all a precognition, and you know to try a different spell. Your spell is expended, but you can Cast a Spell that requires the same number of actions as the triggering spell or fewer to cast. The second spell must be a different spell than the first.

**Source:** `= this.source` (`= this.source-type`)
