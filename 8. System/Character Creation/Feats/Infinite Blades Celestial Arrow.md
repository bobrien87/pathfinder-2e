---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a ranged weapon ikon

Each shot you launch multiplies itself with spiritual blades, rings, and other missiles that shower upon your foes. Your weapon ikon gains the following abilities.

**Immanence** Whenever you successfully Strike an enemy with your weapon ikon, up to two enemies adjacent to the target take spirit damage equal to your weapon ikon's damage dice as they are struck by duplicated missiles.

**Transcendence—[[Heaven Rains an Ending]]** `pf2:3` (transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.JtEzSceixS0WA8wn inline]

**Source:** `= this.source` (`= this.source-type`)
