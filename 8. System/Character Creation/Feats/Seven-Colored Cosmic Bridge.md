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

**Usage** imbued into a melee weapon ikon

Your divine spark shines in a riot of shimmering colors, capable of carrying you through the world as fast as light itself. The imbued ikon gains the following abilities.

**Immanence** (light, teleportation) Your weapon scatters rainbow-colored light across nearby surroundings, each a possible destination. When you successfully Strike an enemy, you can choose to teleport to an unoccupied location within 10 feet as a free action.

**Transcendence—[[Fleeting Arc through Heaven and Earth]]** `pf2:3` (light, spirit, teleportation, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.ObFY26oKlreyVIUm inline]

**Source:** `= this.source` (`= this.source-type`)
