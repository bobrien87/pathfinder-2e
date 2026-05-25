---
type: action
source-type: "Remaster"
traits: ["[[Illusion]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Effect** Your ostilli turns clear as it converts its stored magic into a bubble of refracting light around you. You become [[Hidden]] to all creatures until the end of your turn. If you Strike a creature, that creature is [[Off Guard]] against that attack, and you then become observed.

**Source:** `= this.source` (`= this.source-type`)
