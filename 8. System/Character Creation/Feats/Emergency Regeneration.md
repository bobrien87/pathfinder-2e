---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Healing]]", "[[Primal]]", "[[Vitality]]"]
prerequisites: "Wild Mimic Dedication, you have deactivated a creature's regeneration for at least 1 round or have identified a creature with regeneration in combat"
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You're reduced to 0 hit points from damage that's neither acid nor fire.

You have battled against foes whose bodies naturally regenerate, and while yours doesn't do so all the time, it can happen in a pinch. You gain the effects of a 7th-rank [[Regenerate]] spell. At 20th level, you gain the effects of a 9th-rank *regenerate* instead.

**Source:** `= this.source` (`= this.source-type`)
