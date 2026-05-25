---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Arcane]]", "[[Elf]]"]
frequency: "once per PT1H"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You can prevent demonic foes from fleeing your wrath via teleportation. Make a bow Strike against a demon. In addition to the normal effects of the Strike, the target must attempt a [[Will]] save against your class DC.
- **Critical Success** The target avoids any additional effect.
- **Success** The target takes a –5 circumstance penalty to all their movement Speeds for 1 round as arcane coils of magic meddle with their mobility.
- **Failure** As success, but a –5 foot circumstance penalty for 1 minute. While the target is affected by this, Anchoring Arrow attempts to counteract any teleportation effect that would move the target, or any effect that would transport the target to a different plane. The arrow has a counteract rank of 7th and a +20 modifier to the roll.
- **Critical Failure** As failure, except a –10 foot circumstance penalty, and the duration is 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
