---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sniping Duo|Sniping Duo]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Sniping Duo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You and your spotter take advantage of each other's attacks to momentarily hide and throw your foes off-balance against your follow-up attack. When you successfully Strike a foe using a crossbow or firearm, your spotter can use a reaction to attempt a Stealth check against the foe's Perception DC. On a success, the foe is [[Off Guard]] against the spotter's next attack before the end of your spotter's next turn. Similarly, when your spotter successfully makes a ranged Strike against a foe, you can use a reaction to attempt a Stealth check against the foe's Perception DC. On a success, the foe is off-guard against your next attack against them before the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
