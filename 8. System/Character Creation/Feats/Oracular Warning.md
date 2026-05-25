---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Cursebound]]", "[[Divine]]", "[[Emotion]]", "[[Mental]]", "[[Oracle]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You are about to roll initiative.

You have a premonition about impending danger that you use to warn your allies. Each ally within 20 feet gains a +2 status bonus to their initiative roll and gains temporary Hit Points equal to half your level, which last for 1 minute. If you are [[Cursebound 2]] when you use Oracular Warning, the bonus increases to +3, and if you are cursebound 3, the bonus increases to +4.

> [!danger] Effect: Oracular Warning

**Source:** `= this.source` (`= this.source-type`)
