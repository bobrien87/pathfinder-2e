---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gladiator|Gladiator]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Impressive Performance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to turn combat into a form of entertainment. You gain the Additional Lore general feat for Gladiatorial Lore. If you were already trained in Gladiatorial Lore, you also become trained in a Lore skill of your choice.

At the start of a combat encounter, if you have spectators, you gain a number of temporary HP equal to your character level for 1 minute and you can roll Performance for your initiative. If there are sapient creatures observing a combat encounter, and these onlookers are neither engaged in the combat themselves nor directly assisting any participants, the combatants have spectators. The GM is the final arbiter of whether or not a combat has spectators.

> [!danger] Effect: Gladiator Dedication

Gladiator

**Source:** `= this.source` (`= this.source-type`)
