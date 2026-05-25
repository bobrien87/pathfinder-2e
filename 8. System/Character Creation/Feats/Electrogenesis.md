---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Electricity]]", "[[Primal]]"]
prerequisites: "Wild Mimic Dedication, you have seen a creature deal electricity damage with an unarmed Strike or have identified a creature capable of dealing electricity damage with an unarmed Strike in combat"
frequency: "once per PT10M"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

Some animals and beasts have electric organs in their body that they can use to jolt their prey. You may not have the requisite physiology to do the same, but a touch of primal magic can achieve the same effect. Make a melee unarmed Strike against a creature. If the Strike hits, it deals an additional 1d12 electricity damage, and the creature must make a [[Fortitude]] save against the higher of your class DC or spell DC.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Clumsy]] 1 for 1 round.
- **Failure** The creature is [[Clumsy]] 2 for 1 round.
- **Critical Failure** The creature is [[Clumsy]] 3 for 1 round.

**Source:** `= this.source` (`= this.source-type`)
