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

You signal your team to move into position together. Signal all squadmates; each can immediately Stride as a reaction, though each must end their movement inside your banner's aura, or as close to your banner's aura as their movement Speed allows.

Squadmates can use Gather to Me! while Burrowing, Climbing, Flying, or Swimming instead of Striding if they have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
