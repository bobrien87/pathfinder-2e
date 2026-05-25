---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Inventor]]", "[[Manipulate]]"]
prerequisites: "offensive boost"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You aren't satisfied with keeping to just one kind of boost from your constant tinkering, so you've learned to modulate between several possibilities at once. Choose two additional offensive boosts. You can use an Interact action to change the offensive boost currently affecting your weapon, choosing between the one you chose for the class feature and the two you chose for this modification. If your weapon has the modular trait, you can swap the offensive boost as part of the Interact action you take to use that trait.

**Source:** `= this.source` (`= this.source-type`)
