---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Divine]]", "[[Sanctified]]"]
prerequisites: "Herald's Weapon"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a Strike made with a weapon or unarmed attack empowered by [[Herald's Weapon]].

You call upon your deity's power and channel it through your weapon. The creature you hit in your previous action must attempt a [[Reflex]] save saving throw against the higher of your class DC or your spell DC.
- **Critical Success** The target is unaffected.
- **Success** The target takes @Damage[(floor(@actor.level/2))[spirit]]{spirit damage equal to half your level}.
- **Failure** The target takes @Damage[(@actor.level)[spirit]]{spirit damage equal to your level} and is knocked [[Prone]].
- **Critical Failure** The target takes @Damage[(2*@actor.level)[spirit]]{spirit damage equal to twice your level}, is knocked prone, and becomes [[Clumsy]] 1 until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
