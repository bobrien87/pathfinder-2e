---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Heroic Scion|Heroic Scion]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Heroic Scion Dedication"
frequency: "once per PT1H"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Be they in your current life or your previous one, you've had many heroic moments that continue to inspire you. Even past failures or humiliations can become a source of inspiration—or at least, an opportunity to make up for a past error on this new day. Attempt an Incarnation Lore check against a very hard DC of your level.
- **Critical Success** You gain a +3 status bonus to AC and resistance to physical damage equal to your level until the end of your next turn. You can Sustain this effect for up to 1 minute.
- **Success** As critical success, but the status bonus is +2 and the resistance is equal to half your level.
- **Failure** You gain a +1 status bonus to AC until the end of your next turn.
- **Critical Failure** You gain a +1 status bonus to AC against the next attack made against you until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
