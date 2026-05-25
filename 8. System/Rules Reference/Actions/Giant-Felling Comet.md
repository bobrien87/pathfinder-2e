---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You shoot the [[Starshot]], causing a detonation in a @Template[type:burst|distance:5] within 60 feet. Each creature in the area must succeed at a [[Reflex]] save against your class DC or take spirit damage equal to your normal Strike damage with the starshot. Creatures larger than you take a –2 circumstance penalty to their saving throws. This shot requires any ammunition that would normally be required for the weapon.

**Source:** `= this.source` (`= this.source-type`)
