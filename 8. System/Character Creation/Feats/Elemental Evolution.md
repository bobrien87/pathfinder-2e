---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Barbarian]]"]
prerequisites: "elemental instinct"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The elemental power within you is more mutable and versatile than most. Choose a second damage type for your element. Whenever you Rage, you can choose that type instead of the damage type you would normally gain. The new damage type can be the one you did not choose when you selected the element initially if you had multiple options available for your element, or one of the following types:

**air** cold

**earth** poison

**fire** cold

**metal** electricity

**water** acid

**wood** poison.

**Source:** `= this.source` (`= this.source-type`)
