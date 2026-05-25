---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Alter Ego|Alter Ego]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Alter Ego Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You twist not just the visual, but the auditory as well, allowing you to pass without a sound and create minor noises as distractions—perfect for misdirection and infiltration. You can cast [[Silence]] on yourself as a 2nd-rank innate occult spell and [[Ventriloquism]] as a 1st-rank innate occult spell, each once per day. You also can cast [[Figment]] as an innate occult cantrip. You become trained in the spell attack modifier and spell DC statistics, and your key spellcasting attribute for alter ego archetype spells is Charisma.

**Source:** `= this.source` (`= this.source-type`)
