---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Champion]]"]
prerequisites: "Faithful Steed, unholy"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your mount becomes a grotesque creature of foreboding when you ride it. Its appearance transforms as flames erupt from its skin, a whorl of void energy surrounds it, or poison leaks from its flesh. When you [[Mount]] your faithful steed, you can choose fire, poison, or void. As long as you ride it, your steed gains resistance 10 to the chosen damage type, and any creature that touches your steed takes 1d6 damage of the chosen type; this includes hitting the steed with an unarmed attack or with a melee weapon Strike while adjacent to the steed. This damage increases to 2d6 at 16th level and 3d6 at 20th level.

> [!danger] Effect: Pale Horse

**Source:** `= this.source` (`= this.source-type`)
