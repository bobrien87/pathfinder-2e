---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Auditory]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Yaoguai]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You're in yaoguai form.

You let out a mighty howl, chant of death, or speak with eerie repetition that plants fear in others. All enemies within 30 feet must attempt a [[Will]] save against your class DC or spell DC, whichever is higher.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Frightened]] 1.
- **Failure** The target is frightened 1 and [[Off Guard]].
- **Critical Failure** The target is [[Frightened]] 2 and off-guard.

**Source:** `= this.source` (`= this.source-type`)
