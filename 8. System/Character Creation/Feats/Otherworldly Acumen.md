---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Elf]]"]
prerequisites: "at least one innate spell gained from an elf ancestry feat"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The arcane magic you possess grows in power and complexity. Choose one common 2nd-rank spell from the same tradition as an innate spell you previously gained from another elf ancestry feat (from the arcane list if you have [[Otherworldly Magic]], for example). You can cast that spell as an innate spell once per day, using the same tradition as the list you chose the spell from.

Your magic is adaptable. By spending 1 day of downtime, you can change the spell you chose to a different common 2nd-rank spell from the same tradition.

**Source:** `= this.source` (`= this.source-type`)
