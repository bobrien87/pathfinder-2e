---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Tengu]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A creature within 60 feet uses a fortune or misfortune effect.

As someone tries to twist fate, you consume the interference. The triggering effect is disrupted. If it's a misfortune effect, Eat Fortune gains the fortune trait; if it's a fortune effect, Eat Fortune gains the misfortune trait. This fortune or misfortune applies to the same roll the triggering effect would have, so you couldn't negate a fortune effect with Eat Fortune and then apply a misfortune effect to the same roll.

**Source:** `= this.source` (`= this.source-type`)
