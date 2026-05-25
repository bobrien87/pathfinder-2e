---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You call for an aggressive formation designed for exploiting enemies' vulnerabilities. Signal all squadmates; each can Step as a reaction. If any of your allies ends this movement adjacent to an opponent, that opponent is [[Off Guard]] to melee attacks from you and all other squadmates who responded to Pincer Attack until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
