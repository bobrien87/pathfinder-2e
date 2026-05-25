---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Human]]"]
prerequisites: "spellcasting class feature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through study of multiple magical traditions, you've altered a spell to suit your spellcasting style. Choose one cantrip from a magical tradition other than your own. If you prepare spells, you can choose this spell when you prepare your cantrips, in addition to your other options. If you have a spell repertoire, replace one of your cantrips known with the chosen spell. You can cast this cantrip as a spell of your class's tradition.

If you swap or retrain this cantrip later, you can choose its replacement from the same alternate tradition or a different one.

**Source:** `= this.source` (`= this.source-type`)
