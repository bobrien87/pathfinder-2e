---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Runelord|Runelord]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Downtime]]", "[[Skill]]"]
prerequisites: "Runelord Dedication, trained in Crafting"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You discover the secrets to embedding aeon stones into your flesh. You spend 1 day attuning to an aeon stone and physically embedding it in your skin. While the stone is embedded this way, you gain the benefits of the aeon stone as if it were orbiting above your head, but it protects the stone from being noticed or stolen as easily. Aeon stones in your flesh must be invested to function, as usual.

You can also use this activity to safely remove an embedded aeon stone in 1 day. Someone without this feat can attempt to surgically remove it safely by spending 1 day and succeeding at a DC 30 [[Medicine]] check, or hastily by simply ripping it from a corpse.

**Source:** `= this.source` (`= this.source-type`)
