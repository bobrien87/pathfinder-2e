---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Fighter]]"]
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your training allows you to shrug off your foes' spells and conditions when the need is dire. Choose a single nonpermanent condition, spell, or magical effect that is affecting you. If you chose a condition, its effect on you ends. If you chose a spell or other magical effect, attempt to counteract the spell (your counteract rank is equal to half your level, rounded up, and you attempt a Will save as your counteract check).

This doesn't remove any Hit Point damage you already took from the spell or condition, and it removes the effect from only you, not from other creatures or the environment around you. It can't remove an ongoing affliction or prevent such an affliction from inflicting conditions on you later. It can't remove conditions occurring automatically due to your situation or positioning (such as [[Prone]] or flanked).

**Source:** `= this.source` (`= this.source-type`)
