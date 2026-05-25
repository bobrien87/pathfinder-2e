---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Commander]]", "[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An adjacent enemy begins to use a reaction.

**Commander** Your own tactical expertise allows you to quickly identify and prevent enemy responses. If the triggering creature's level is equal to or lower than yours, you disrupt the triggering reaction. If the triggering creature's level is higher than yours, make an attack roll against its AC. On a success, you disrupt the reaction.

**Rogue** Grabbing a sleeve, swiping with your weapon, or creating another obstruction, you reflexively foil an enemy's response. If the triggering creature's level is equal to or lower than yours, you disrupt the triggering reaction. If the triggering creature's level is higher than yours, you must make an attack roll against its AC. On a success, you disrupt the reaction.

**Source:** `= this.source` (`= this.source-type`)
