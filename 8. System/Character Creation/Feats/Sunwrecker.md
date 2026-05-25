---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into any weapon ikon

Your weapon has the might of legends, capable of shooting or striking any light out of the sky. The imbued ikon gains the following abilities.

**Immanence** (darkness) on a successful critical hit with the weapon, the weapon casts 2nd-rank [[Darkness]] centered on the target of the attack.

**Transcendence—[[Break the Sun's Legs]]** `pf2:2` (cold, concentrate, darkness, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.Y9XUwC8ihxZCfndG inline]

**Source:** `= this.source` (`= this.source-type`)
