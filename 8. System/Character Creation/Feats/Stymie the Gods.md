---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Godling Dedication"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

By exerting your will as a nascent god present in the mortal realms, you can hold off the influences of most distant entities, even ones much older and more powerful than yourself. Either you or your hierophant are able to use this action. When either of you do, you both gain a +2 status bonus to Armor Class and saving throws against divine spells, as well as the spells, Strikes, and abilities of extraplanar creatures, for 3 rounds. This benefit affects both you and your hierophant even if you are on separate planes of existence when this ability is used.

If a Mythic Point is spent by the individual using Stymie the Gods, the bonus increases to +4 and the effects last for 10 minutes

> [!danger] Effect: Stymie the Gods

**Source:** `= this.source` (`= this.source-type`)
