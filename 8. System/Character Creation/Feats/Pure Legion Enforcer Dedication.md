---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pure Legion Enforcer|Pure Legion Enforcer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "member of the Pure Legion"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are sworn to uphold the Laws of Mortality within the borders of Rahadoum. As part of your commissioning, you learned about the different types of worship and divine magic that you might encounter. You become trained in Intimidation and Religion. If you are already trained in one or both of these skills, you become an expert in that skill. If you are already an expert in both skills, you become trained in a skill of your choice.

You also gain the [[Recognize Spell]] skill feat. Whenever you attempt to recognize a divine spell, you always learn it is divine and gain a +2 circumstance bonus to the Religion skill check.

Finally, you gain the following edicts and anathema. Knowingly committing acts that violate the anathema result in you losing access to abilities granted by this archetype, as determined by your GM. You can regain these lost abilities by spending an appropriate amount of time rededicating yourself to the Pure Legion, typically by donating an amount equal to 20 gp × your level to appropriate causes and eschewing all divine magic (including spells cast by others) for at least 1 day.

**Edicts** confiscate, contain, or destroy all divine objects in Rahadoum; drive out divine casters from Rahadoum

**Anathema** use divine abilities, items, or spells; permit proselytizing of religion in Rahadoum; worship a deity

Pure Legion Enforcer

**Source:** `= this.source` (`= this.source-type`)
