---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Goblin]]", "[[Occult]]"]
prerequisites: "dokkaebi goblin heritage"
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can summon a mass of magic energy in your hand that, naturally, you use to smack those who offend you. You conjure forth a spectral bangmangi club for 1 minute, which appears in your hands, though you can give it to another creature to wield. This weapon is a *+1 striking ghost touch club*.

At 13th level, the bangmangi is a *+2 greater striking ghost touch club*.

**Source:** `= this.source` (`= this.source-type`)
