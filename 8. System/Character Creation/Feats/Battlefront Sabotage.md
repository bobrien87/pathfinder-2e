---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Incapacitation]]"]
prerequisites: "Guerrilla Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a free hand.

You know methods of sabotaging your enemy's war machines and weaponry. You can attempt to sabotage a siege weapon or vehicle with a [[Thievery]] check against the standard DC of the weapon or vehicle's level.
- **Critical Success** The next time the weapon is Launched or the vehicle moves, it targets or moves to a square of your choice instead of its intended target.
- **Success** As critical success, but the weapon or vehicle targets or moves to a random square.
- **Failure** The sabotage fails.

Additionally, you can use Battlefront Sabotage to sabotage a weapon an enemy is wielding. Choose a creature wielding a melee or ranged weapon within your reach and attempt a Thievery check against their Reflex DC. On a success, the weapon's wielder must succeed at a DC 11 flat check the next time it attempts a Strike with that weapon or the action is disrupted, as part of the weapon's structural integrity falters. The creature is then temporarily immune to Battlefront Sabotage of their weapons for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
