---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lion Blade|Lion Blade]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Lion Blade Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You succeed at a save against a detection, mental, or scrying effect.

You've learned how to analyze and fake your responses to the most common magic used against spies. You can attempt to identify the effect via [[Identify Magic]] using the magical tradition skill of the effect or Espionage Lore, even if you didn't notice the spell being cast.

If you successfully identify the triggering effect, and it would normally fail or have no effect, you can make the caster of the triggering effect think the effect or spell succeeded. If they would obtain a result, such as receive a piece of information, you decide what that result is. If the effect would influence you to take certain actions, you can make it appear as if you were affected and attempt to play along; if the effect normally establishes a mental link, it functions normally, but you can disregard any commands you receive through the link.

**Source:** `= this.source` (`= this.source-type`)
