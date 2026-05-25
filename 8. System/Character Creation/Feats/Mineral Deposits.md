---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Dragonblood]]"]
prerequisites: "Terra Dragonblood"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Precious metals from your bloodstream line your claws, jaws, or the tip of your tail, and you're able call upon your blood to surge and empower your attacks. Choose cold iron or silver and a claw, jaws, or tail unarmed attack that you have. Until the end of your turn, your Strikes with the chosen unarmed attack count as being made of the chosen metal. At 17th level, you can choose adamantine.

**Source:** `= this.source` (`= this.source-type`)
