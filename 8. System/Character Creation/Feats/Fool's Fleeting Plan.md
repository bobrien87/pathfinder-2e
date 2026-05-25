---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Mythic]]"]
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When Aercelys, hero-god of fools and fire, dove into the funeral pyre of his beloved daughter, he seemed a fool without thought for his safety. Yet when he returned with her body, he showed the slow rise of her chest, and those who doubted became the fools.

You carry Aercelys's spark within you, which protects you from rash decisions. You do not trigger reactions when you use an action that you gained from being [[Quickened]].

**Source:** `= this.source` (`= this.source-type`)
