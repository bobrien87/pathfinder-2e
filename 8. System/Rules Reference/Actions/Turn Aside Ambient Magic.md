---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your ostilli glows a faint yellow as it establishes a barrier. Choose acid, cold, electricity, fire, or sonic damage. Until the beginning of your next turn, you gain resistance against the chosen damage type equal to half your level.

**Source:** `= this.source` (`= this.source-type`)
