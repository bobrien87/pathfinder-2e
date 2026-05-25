---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You aim your weapon in a superficial cut above your opponent's eye. Make a Strike with the imbued ikon. If that Strike is successful, the target must succeed at a [[Fortitude]] save against your class DC or become [[Blinded]] for 1 round or until it uses an Interact action to clear the blood from its vision.

**Source:** `= this.source` (`= this.source-type`)
