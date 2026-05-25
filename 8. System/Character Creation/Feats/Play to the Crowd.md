---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gladiator|Gladiator]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Gladiator Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You reduce an enemy to 0 Hit Points during a non-trivial combat encounter with spectators.

You show off for the crowd. Attempt a Performance check; the DC is determined by the GM but is typically the standard DC for your level or the DC to [[Make an Impression]] on the spectators, whichever is higher. On a success, choose one of the following benefits; on a critical success, choose two benefits:

- A number of temporary Hit Points equal to your character level; these last for 1 minute.

> [!danger] Effect: Play to the Crowd (Temporary Hit Points)

- A +1 circumstance bonus to AC until the end of your next turn.

> [!danger] Effect: Play to the Crowd (AC Bonus)

- A +1 circumstance bonus to your next attack roll before the end of your next turn.

> [!danger] Effect: Play to the Crowd (Attack Roll Bonus)

**Source:** `= this.source` (`= this.source-type`)
