---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Emotion]]", "[[Manipulate]]", "[[Mental]]", "[[Merfolk]]", "[[Primal]]", "[[Visual]]"]
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You weep, and your tears become gleaming pearls as they fall to the ground, so beautiful others can't help but grab at them. All creatures adjacent to you must attempt a [[Will]] save against the higher of your class DC or spell DC. The pearls dissolve at the start of your next turn, turning into salt water.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Slowed]] 1 until the start of your next turn as it covets the pearls or reaches for them.
- **Failure** The target is slowed 1 until the start of your next turn as it grabs for the pearls, and if it doesn't have a free hand (or similar appendage), it must spend its first action on its next turn to Release one item it's holding.
- **Critical Failure** As failure, but the target is [[Slowed]] 2 instead of slowed 1.

**Source:** `= this.source` (`= this.source-type`)
