---
type: action
source-type: "Remaster"
traits: ["[[Primal]]", "[[Teleportation]]", "[[Water]]"]
cast: "`pf2:2`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per minute

**Requirements** You're on land and adjacent to a body of water

**Effect** You sink into the water and emerge back onto land in another space within 120 feet that's adjacent to the same body of water. You can transport yourself, any items you're wearing and holding, and up to one other willing creature.

**Source:** `= this.source` (`= this.source-type`)
