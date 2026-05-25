---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You open yourself to the guidance of whatever spirits or powers deign to help you. Roll 1d4 to see what type of spirit is drawn to you. Your next action must be the type of action the spirit prefers, but you also gain the listed benefit for the action as the spirit guides you. If you attempt to use a different action, you must succeed at a DC 6 flat check or the action is lost.

**1 Warrior** You must attempt a Strike. You gain a +1 status bonus to your attack roll and a +2 status bonus to damage, or a +6 status bonus to damage if you are at least [[Cursebound 3]].

**2 Adept** You must attempt a Perception check or a skill action. You gain a +1 status bonus to the check, or a +2 status bonus if you are cursebound 3.

**3 Sage** You must attempt to Cast a Spell. You gain a status bonus to the spell's damage or healing equal to the spell's rank, or equal to the spell's rank + 3 if you are at least cursebound 3.

**4 Wanderer** You must attempt a Stride action, or a Fly, Climb, or Burrow action if you have the relevant speed. You gain a +10-foot status bonus to your Speed for the action, or a +20-foot status bonus if you are at least cursebound 3.

**Source:** `= this.source` (`= this.source-type`)
