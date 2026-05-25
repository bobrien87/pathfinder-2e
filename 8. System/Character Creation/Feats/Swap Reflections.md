---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Alter Ego|Alter Ego]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Extradimensional]]", "[[Incapacitation]]", "[[Occult]]", "[[Teleportation]]"]
prerequisites: "Alter Ego Dedication"
frequency: "once per PT10M"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You've learned how to use even your reflection to your advantage. You send your own reflection to forcibly swap places with the reflection of an enemy, pulling each of you through opposite ends and switching places. The enemy must be within 120 feet, you must both be adjacent to reflective surfaces (such as glass, mirrors, or calm water), and you must be able to see the target's reflection and have line of effect to it. The target attempts a [[Will]] save against your spell DC or class DC, whichever is higher.
- **Critical Success** The spell has no effect.
- **Success** You swap positions with your target or arrive adjacent to your target, whichever your target prefers.
- **Failure** You swap positions with your target or arrive adjacent to your target, whichever you prefer.
- **Critical Failure** You instantaneously swap positions with your target, and the target becomes trapped in its own reflection for 1 minute. Once on each of its turns, the target can spend 1 action to attempt another Will save to escape. If the save succeeds, the effect ends early.

**Source:** `= this.source` (`= this.source-type`)
