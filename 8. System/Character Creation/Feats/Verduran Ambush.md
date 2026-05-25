---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Verduran Shadow|Verduran Shadow]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Verduran Shadow Dedication, expert in Stealth"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You prepare to ambush a foe. You Ready an activity that takes 2 actions, though that activity must either be Death from Above or an activity with the requirement that you be [[Hidden]] or [[Undetected]] by all your opponents (such as [[Scout's Pounce]]). After using the reaction, you cannot use this feat again for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
