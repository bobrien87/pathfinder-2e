---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warrior Of Legend|Warrior Of Legend]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Warrior of Legend Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You are [[Doomed]] 1 or greater and your [[Dying]] value would increase.

As your legend grows, details of your demise become clearer. And you know that it is not yet your time. You can attempt a recovery check using your dying value before it increases, rolling twice and taking the better result. Regardless of the outcome, reduce your doomed value by 1.

**Source:** `= this.source` (`= this.source-type`)
