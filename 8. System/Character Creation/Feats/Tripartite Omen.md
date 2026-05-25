---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Halcyon Speaker|Halcyon Speaker]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "Dualistic Synergy, Shattered Sacrament, master in Religion"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You invoke religious portents to ward yourself against danger without losing sight of the history that led to this point. When you use [[Dualistic Synergy]], if your next action is to Cast a Spell from your spell slots and that spell is divine, you gain a +1 status bonus to AC for 1 round. If the spell is a halcyon spell, you gain this benefit in addition to the benefits described in Dualistic Synergy.

> [!danger] Effect: Tripartite Omen

**Source:** `= this.source` (`= this.source-type`)
