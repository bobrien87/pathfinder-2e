---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Divine]]", "[[Oracle]]", "[[Secret]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You tap into the collected lore of the divine, accessing a variety of potentially useful information.

Attempt a [[Religion]] check to understand the information you gain. The GM sets the DC (similar to the DC to [[Recall Knowledge]]), potentially adjusting the DC of the check for topics far removed from your mystery.
- **Critical Success** You comprehend the lore accurately or gain a useful clue from the divine about your situation.
- **Success** You learn two pieces of information about the topic, one true and one erroneous, but you don't know which is which.
- **Failure** You recall incorrect information or gain an erroneous or misleading clue.
- **Critical Failure** You recall two pieces of incorrect information or gain two erroneous or misleading clues.

**Source:** `= this.source` (`= this.source-type`)
