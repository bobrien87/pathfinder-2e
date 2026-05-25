---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Merfolk]]", "[[Primal]]"]
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Sailors know that the sight of an angry merfolk might well mean that they never see the shore again. You sing a song that foretells the fate of a creature you can see within 60 feet. The fear that grips the target's soul causes 10d10 mental damage, depending on the target's [[Will]] save against the higher of your class DC or spell DC. A creature who's in the water or onboard a seagoing vessel takes a –4 circumstance penalty to its saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and is [[Frightened]] 1 as it glimpses its demise.
- **Failure** The target takes full damage and is frightened 1. In addition, it rolls twice for all skill checks and saving throws it attempts until the end of its next turn and takes the worse result; this is a misfortune effect.
- **Critical Failure** As failure, except double damage and [[Frightened]] 2.

**Source:** `= this.source` (`= this.source-type`)
