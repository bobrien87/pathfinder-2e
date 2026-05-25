---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lion Blade|Lion Blade]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "member of the Lion Blades, trained in Performance"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're from Taldor.

Your Lion Blade spy training helps you conceal yourself and your identity. You become trained in your choice of Deception or Stealth; if you were already trained in that skill, you become an expert instead. You also gain the [[Additional Lore]] skill feat for Espionage Lore. If you were already trained in Espionage Lore, you also become trained in a Lore skill of your choice.

You never take circumstance penalties for attempting to take a disguise of a different ancestry, age, and so on, as long as the disguised form is appropriate for your size.

Lion Blade

**Source:** `= this.source` (`= this.source-type`)
