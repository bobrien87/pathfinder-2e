---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pure Legion Enforcer|Pure Legion Enforcer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Linguistic]]"]
prerequisites: "Pure Legion Enforcer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You recite an excerpt of the Laws of Mortality, often the first law: "Let no mortal be beholden to a god." Attempt an [[Intimidation]] check against all enemies within 60 feet that worship a deity, comparing your result against each target's Will DC. Targets are then temporarily immune to your use of this ability for 24 hours.
- **Critical Success** The target becomes [[Frightened]] 2. Until the start of your next turn, if the target attempts to Cast a Spell with the divine trait, it must succeed at a DC 7 flat check or the action is lost.
- **Success** As critical success, but [[Frightened]] 1, and the DC of the flat check is 5.

> [!danger] Effect: Edict of Mortality

**Source:** `= this.source` (`= this.source-type`)
