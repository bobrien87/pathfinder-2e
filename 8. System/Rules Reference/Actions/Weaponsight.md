---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Magical]]"]
cast: "`pf2:1`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Close your eyes and concentrate on your warshard weapon. You perceive the world as if you were observing it from your weapon rather than your own eyes. You can see in all directions simultaneously and therefore can't be flanked. If you're not holding your weapon, this ability fails if your warshard weapon is on a different plane than you. If you spend a Mythic Point as part of this action, you attempt saving throws against visual effects at mythic proficiency while observing through your warshard weapon. You can observe through your weapon for up to 1 minute or until you open your eyes as a free action, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
