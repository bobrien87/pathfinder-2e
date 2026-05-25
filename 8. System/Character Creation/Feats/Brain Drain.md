---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mental]]", "[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a wresting of will, you siphon off a creature's mental energy to replenish your own. One non-mindless creature within 30 feet must attempt a [[Will]] save against your spell DC.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Stupefied 1]] for 1 minute, and you regain 1 Focus Point, up to your normal maximum. You can't use Brain Drain again until after the next time you make your daily preparations.
- **Critical Failure** As failure, but the creature is [[Stupefied 2]].

**Source:** `= this.source` (`= this.source-type`)
