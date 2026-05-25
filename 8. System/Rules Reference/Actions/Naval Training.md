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

Your instructions make it easier for you and your allies to swim through dangerous waters. Signal all squadmates; until the end of your next turn, you and each ally gain a swim Speed of 20 feet.

> [!danger] Effect: Naval Training

**Special** If you have this tactic prepared, you can use Warfare Lore in place of Athletics for checks you make to Swim.

**Source:** `= this.source` (`= this.source-type`)
