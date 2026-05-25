---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Leshy]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Access** peachchild leshy heritage

You have a talent for making friends through simple kindness, often among stray animals or other creatures that people tend to overlook, and your inherent magic can make these acts take on additional power. As an Interact action, you can feed a small treat, such as a millet dumpling, to an animal that has an indifferent or better attitude toward you. For the next 1 minute, one of the animal's unarmed attacks becomes a *+1 striking* unarmed attack. If it was already a *+1 striking* attack, it instead gains the effects of the *ghost touch* rune.

**Source:** `= this.source` (`= this.source-type`)
