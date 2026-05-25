---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Red Mantis Assassin|Red Mantis Assassin]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Achaekek's Grip, Basic Red Mantis Magic"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

To resurrect a creature you've slain, a spellcaster must counteract your influence on its death. The DC of this check is equal to your class DC or spell DC, whichever is higher.

In addition, you've undergone training to better make use of your magic. Increase the spell slots you gain from Red Mantis assassin archetype feats by 1 for each spell rank other than your two highest Red Mantis spell slots. You can prepare only spells from the Red Mantis magic school curriculum in these extra slots.

**Source:** `= this.source` (`= this.source-type`)
