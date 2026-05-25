---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Fortune]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day;

**Trigger** You fail or critically fail a Deception, Diplomacy, Intimidation, or Society check

**Effect** Reroll the skill check. You must use the second result, even if it's worse.

**Source:** `= this.source` (`= this.source-type`)
