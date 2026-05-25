---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Fortune]]", "[[Nephilim]]"]
prerequisites: "Aeonbound"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You would critically fail a skill check or suffer an effect with the misfortune trait.

You shift the underlying fabric of reality to impose a baseline of order. If the trigger was a skill check, you instead receive a result of 10 + your proficiency bonus (don't apply any other bonuses, penalties, or modifiers). If the trigger was an effect with the misfortune trait, the misfortune and fortune effects cancel each other out as normal, negating the triggering misfortune effect.

**Source:** `= this.source` (`= this.source-type`)
