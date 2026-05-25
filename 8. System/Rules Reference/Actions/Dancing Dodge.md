---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:r`"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You're hit by a Strike during the first round of combat

**Effect** You take advantage of the fact that your foe isn't ready to anticipate your dance-like moves in combat. Add a +3 circumstance bonus to your Armor Class against the triggering Strike to determine the Strike's actual result.

**Source:** `= this.source` (`= this.source-type`)
