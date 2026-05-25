---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
frequency: "once per PT10M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Requirements** You are riding your apocalypse mount.

You inspire your allies to greater battle prowess while trampling enemies in your way. You Command your apocalypse mount to Stride up to twice its Speed (or to Burrow, Climb, Fly, or Swim, if it has the corresponding movement type), moving through the space of any foes in your path up to one size smaller than your apocalypse mount. Your mount deals damage equal to one of its unarmed attack Strikes to each creature whose space you move through ([[Reflex]] save against your apocalypse mount's Athletics DC). On a critical failure, the creature also becomes [[Off Guard]] until the end of your next turn. You can damage a given creature only once during this movement.

In addition, all allies who witnessed your charge gain a number of temporary Hit Points equal to your level and a +2 status bonus to damage against any foe damaged by your apocalypse mount this round. This has the visual trait. These benefits last until the end of your next turn.

> [!danger] Effect: To War!

**Source:** `= this.source` (`= this.source-type`)
