---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Morph]]", "[[Occult]]", "[[Reflection]]"]
prerequisites: "Morph-Risen"
frequency: "once per PT1M"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** You hit a creature with a melee Strike on your last action.

You channel some of your own nature through your blow, temporarily warping your target's form to resemble your own. The creature you hit must attempt a [[Fortitude]] save against the higher of your class DC or spell DC.
- **Critical Success** The target is unaffected.
- **Success** The target resists the effect but its form twists in the process. It's [[Clumsy]] 1 until the end of its next turn.
- **Failure** The target's body briefly warps to resemble yours. It's clumsy 1 until the end of its next turn and [[Sickened]] 1.
- **Critical Failure** The target's body warps to resemble yours for a significant time. It's clumsy 1 for 1 minute and [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
