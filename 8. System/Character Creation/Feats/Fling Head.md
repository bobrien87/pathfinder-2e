---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ghost|Ghost]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Manipulate]]"]
prerequisites: "Headless Haunt"
frequency: "once per PT1M"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You Interact to remove your head, if it isn't already detached, and fling it at an enemy within 30 feet, where it emits a bone-chilling wail before dematerializing and returning to your body. Your target must attempt a [[Will]] save against your class DC or spell DC, whichever is higher. You can affect one additional creature within 20 feet of your original target for each additional action you spend.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2 and can't reduce their frightened value below 1 while they remain within 30 feet of you.
- **Critical Failure** As failure, but the creature is [[Frightened]] 3.

**Source:** `= this.source` (`= this.source-type`)
