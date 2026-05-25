---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sterling Dynamo|Sterling Dynamo]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Sterling Dynamo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Ustalav.

You've modified your dynamo with Stasian coils, allowing you to make a powerful attack that crackles with electricity. Make a dynamo Strike. On a success, the Strike deals an additional 1d12 electricity damage to the target, as well as @Damage[(ternary(gte(@actor.level,18),2,1))d4[electricity]] damage to up to two other foes within 10 feet as sparks leap across the gaps. If you critically fail your dynamo Strike, you take 1d12 electricity damage. This counts as two attacks when calculating your multiple attack penalty. At 18th level, the additional electricity damage to the target increases to 2d12, and the additional electricity damage to the other foes increases to 2d4. Reduce the operational time of your sterling dynamo by 1 hour.

**Source:** `= this.source` (`= this.source-type`)
