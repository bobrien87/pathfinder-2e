---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Nephilim]]"]
prerequisites: "Aeonbound"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You're afflicted by a disease or poison, or are taking persistent damage.

Your ordered physiology rejects unwelcome elements, allowing you to reject the negative effects of poisons and diseases or shrug off other lasting negative effects. Choose one.

**Disease or Poison** Attempt a saving throw against the affliction. On a failure or critical failure, the affliction's stage doesn't increase.

**Persistent Damage** Attempt a flat check to recover from the persistent damage.

**Source:** `= this.source` (`= this.source-type`)
