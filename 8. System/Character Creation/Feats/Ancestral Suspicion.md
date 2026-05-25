---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Elf]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Long-lived elves have seen civilizations rise and fall, often at the hands of outside forces. As a result, they have developed a wariness of others who might seek to influence or control them. You've been trained to resist such manipulation, gaining a +2 circumstance bonus to saving throws against effects that would make you [[Controlled]], such as [[Dominate]], and to Perception checks to [[Sense Motive]] when trying to determine if a creature is under the influence of such an effect. When you roll a success on a saving throw against such an effect, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
