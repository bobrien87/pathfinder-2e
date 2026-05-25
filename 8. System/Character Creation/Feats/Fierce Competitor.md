---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Centaur]]", "[[Mental]]"]
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You challenge a single ally to a physical competition. This competition must involve accomplishing a specific goal for a specific use of the Acrobatics or Athletics skill, such as [[Climbing]] to the top of a wall, [[Tripping]] a specific foe, or [[Long Jumping]] across a chasm. You and your selected ally gain a +2 circumstance bonus to the associated skill check for 1 minute or until one of you wins the challenge, whichever is first. If you win this competition, you gain a +2 status bonus to Intimidation checks for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
