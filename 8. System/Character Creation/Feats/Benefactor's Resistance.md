---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kobold]]"]
prerequisites: "dragonscaled kobold heritage"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your scales have taken on the characteristics of your draconic benefactor and insulate you from certain damage types. You gain resistance equal to half your level to the damage type dealt by the breath of your draconic benefactor.

If your draconic benefactor's breath deals bludgeoning, piercing, or slashing damage, instead of gaining resistance to that type, you must choose acid, cold, fire, electricity, or sonic.

**Source:** `= this.source` (`= this.source-type`)
