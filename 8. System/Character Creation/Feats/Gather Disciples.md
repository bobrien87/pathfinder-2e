---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starstone Aspirant|Starstone Aspirant]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Starstone Aspirant Dedication, master in Religion"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Gods need followers, and you know that its best to gather a flock in the present to support you in your endeavor. Of course, you'll reward their faith in you in the future when you become a true deity. You can spend 1 week of downtime in a settlement to evangelize your coming godhood and establish a small group of disciples to your faith. Once this group has been established, these disciples are always helpful to you. You can use Religion to `act request skill=religion` something of them, though your request must be able to be performed by the type of people who would follow you, at the GM's discretion. If you critically succeed at this check, your disciples give a piece of helpful advice or let you in on a small secret, granting you or a member of your party a +2 circumstance bonus to the first skill check you attempt when acting on the favor. If you critically fail this check, your disciples' attitude toward you doesn't worsen.

You can have three groups of disciples at any one time (or five if you're legendary in Religion). If you exceed this number, the oldest group disbands and must be established again if you return to that settlement.

> [!danger] Effect: Gather Disciples

**Source:** `= this.source` (`= this.source-type`)
