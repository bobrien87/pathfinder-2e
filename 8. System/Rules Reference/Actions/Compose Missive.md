---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Manipulate]]"]
cast: "Passive"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You spend 10 minutes drawing, writing, or inscribing, covering the missive's surface with text, images, or embossing.

**Source:** `= this.source` (`= this.source-type`)
