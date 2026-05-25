---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Seneschal|Seneschal]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "seneschal witch"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As you work to understand the connection with your missing patron, it's increasingly easy to form bonds with those around you. Raw magical energy spills easily through the connection but, without a patron's control, it sometimes resists your demands for it to form proper spells.

You gain the Witch's Charge feat, but can't choose your familiar or another creature with the minion trait as a charge. When you cast or Sustain manifest will, as long as your charge is within 30 feet, you can choose to center the spell's emanation on your charge instead of yourself.

Seneschal

**Source:** `= this.source` (`= this.source-type`)
