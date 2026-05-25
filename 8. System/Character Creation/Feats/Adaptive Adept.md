---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Human]]"]
prerequisites: "Adapted Cantrip, can cast 3rd rank spells"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've continued adapting your magic to blend your class's tradition with your adapted tradition. Choose a cantrip or 1st-rank spell from the same magical tradition as your cantrip from Adapted Cantrip. You gain that spell, adding it to your spell options just like the cantrip from Adapted Cantrip. You can cast this spell as a spell of your class's magical tradition. If you choose a 1st-rank spell, you don't gain access to the heightened versions of that spell, meaning you can't prepare them if you prepare spells and you can't learn them or select the spell as a signature spell if you have a spell repertoire.

**Source:** `= this.source` (`= this.source-type`)
