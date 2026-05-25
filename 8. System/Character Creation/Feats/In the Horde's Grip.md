---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Necrologist|Necrologist]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Flourish]]"]
prerequisites: "Grasping Corpses"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When your skeletons and zombies attack, their skeletal claws and rotting hands clutch and tear flesh. Weaker foes are caught in their grip. You command your horde to perform a [[Mobbing Assault]]. Instead of being [[Off Guard]], a creature who takes physical damage from failing the saving throw is [[Grabbed]] by your horde ([[Restrained]] on a critical failure). The DC to [[Escape]] from your horde is equal to your spell DC. Creatures grabbed by your horde that fail a saving throw against the horde's Mobbing Assault take 2d6 persistent,bleed damage.

**Source:** `= this.source` (`= this.source-type`)
