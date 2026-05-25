---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Captain|Captain]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Captain Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your followers' skills have developed over the course of your adventures. All your followers become experienced followers.

Additionally, your followers have grown accustomed to the perils of battle, developing the confidence to attack foes without your direction. During an encounter, even if you don't use the [[Direct Follower]] action, your active follower spend can still use 1 action that round on your turn to Stride or Strike. They can do this at any point during your turn, as long as you aren't currently taking an action. If they do, that's all the actions they get that round—you can't Direct them later.

**Source:** `= this.source` (`= this.source-type`)
