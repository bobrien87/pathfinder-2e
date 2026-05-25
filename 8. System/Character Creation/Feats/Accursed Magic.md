---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Curse Maelstrom|Curse Maelstrom]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Curse Maelstrom Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When the curse within you spills out, you can lay curses on others and claim them for yourself with ease. You can cast [[Claim Curse]]. At 10th level, you can also cast [[Seal Fate]], and at 12th level, you can also cast [[Inevitable Disaster]]. You can cast these spells once per day as occult innate spells, but only while within your curse maelstrom state. If you couldn't already cast occult spells, these spells use Wisdom as your spellcasting attribute, and you become trained in the spell attack modifier and spell DC statistics.

**Source:** `= this.source` (`= this.source-type`)
