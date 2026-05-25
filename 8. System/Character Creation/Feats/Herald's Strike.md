---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]", "[[Sanctified]]", "[[Spirit]]"]
prerequisites: "Herald's Weapon"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The power of your blows can send your victim hurling through your deity's realm for a fragment of a second. You activate Herald's Weapon, ignoring the frequency, and make a Strike with your transformed weapon or unarmed attack against a creature. If you hit and deal damage, the target must attempt a [[Will]] save against the higher of your class DC or spell DC. If your Strike was a critical hit, the creature uses the outcome for one degree of success worse than the result of their saving throw. Regardless of the result, the target becomes immune to Herald's Strike for 10 minutes.
- **Critical Success** The target is unaffected.
- **Success** The target takes 3d10 spirit damage and becomes [[Dazzled]] for 1 round.
- **Failure** The target takes 6d10 spirit damage and becomes dazzled for 1 round and [[Drained]] 1.
- **Critical Failure** The target takes 12d10 spirit damage and becomes [[Blinded]] for 1 round and [[Drained]] 2.

**Source:** `= this.source` (`= this.source-type`)
