---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Regardless of your individual strengths, collectively your squad has the power to move mountains and topple giants. Signal a squadmate within the aura of your commander's banner. That squadmate can attempt to [[Reposition]], [[Shove]], or [[Trip]] a target within their reach. Each other squadmate who is adjacent to the original squadmate or the target can attempt to assist with the maneuver as a reaction

For each squadmate who assists in this way, the original squadmate increases the maximum size of creature they can target (for example, if a total of two squadmates participated in this maneuver, the initial squadmate could target a creature up to two sizes larger than them.) The original squadmate gains a circumstance bonus on their check to Reposition, Shove, or Trip equal to the number of additional squadmates who assisted in the maneuver (maximum +4).

> [!danger] Effect: The Bigger They Are (Commander)

**Source:** `= this.source` (`= this.source-type`)
