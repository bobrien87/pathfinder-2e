---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Monk]]", "[[Occult]]", "[[Water]]"]
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Never distant from water's succoring presence, your refined breathing techniques focus your awareness and control of water inward. You gain a +2 circumstance bonus to Will saves and saves against poison until the beginning of your next turn. If you spent two actions on Tributary Circulation, you can also attempt a flat check to end persistent poison damage you're suffering, reducing the DC to 10 as if you had gained the benefits of assisted recovery.

**Source:** `= this.source` (`= this.source-type`)
