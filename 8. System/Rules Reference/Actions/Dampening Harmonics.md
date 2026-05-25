---
type: action
source-type: "Remaster"
traits: ["[[Magical]]"]
cast: "`pf2:2`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** You establish a force field that grants you resistance 10 to damage dealt by spells and magical abilities with the trait of your magiphage ability, except for force damage. The force field lasts for 10 minutes. Each time the field prevents damage, the duration decreases by 1 minute.

**Source:** `= this.source` (`= this.source-type`)
