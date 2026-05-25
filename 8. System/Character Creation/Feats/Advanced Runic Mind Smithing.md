---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mind Smith|Mind Smith]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Runic Mind Smithing"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your mind can hold onto more complicated patterns than ever before. You can etch the greater forms of any runes on the list from the Runic Mind Smithing feat and add them to the list of options you can choose during your daily preparations, as well as the *holy* or *unholy* runes.

In addition, once per day, you can spend 10 minutes of uninterrupted focus to swap your daily prepared rune from Runic Mind Smithing to another rune from the same list. Once this swap is made, that second rune remains on the weapon until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
