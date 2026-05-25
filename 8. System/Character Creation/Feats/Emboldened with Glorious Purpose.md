---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Emissary|Rivethun Emissary]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Fortune]]", "[[Mental]]"]
prerequisites: "Consults the Spirits"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Communing with powerful spirits of the world and other powers far greater than yourself fills your heart with purpose and inspires you to strive for greater accomplishments. Whenever you Consult the Spirits, you gain a +1 status bonus to Will saving throws until the next time you make your daily preparations. This bonus increases to +2 against emotion and fear effects.

In addition, until the next time you make your daily preparations, you can do each of the following once.

- Roll a Will save twice and use the better result.
- Roll an attack roll twice and use the better result.
- Roll a skill check twice and use the better result; this skill check must be made with the skill that the spirits blessed during Consult the Spirits.

**Source:** `= this.source` (`= this.source-type`)
