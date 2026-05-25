---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Champion]]", "[[Oath]]"]
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

During your daily preparations, you can swear an oath to defend against a certain kind of enemy during your deeds that day. Choose aberrations, celestials, dragons, fiends, or undead. You can't choose celestials if you're holy, nor can you choose fiends if you're unholy. You gain an edict to defend against creatures of that kind.

Allies in your champion's aura, not including you, get resistance 2 to damage dealt by creatures with the chosen trait. If such a creature deals more than one damage type at once, apply this resistance only to the highest amount of damage. The resistance increases to 3 at 7th level, 4 at 12th level, and 5 at 17th level. If a creature with the chosen trait triggers your champion's reaction and your champion's reaction grants resistance against the triggering damage, the resistance increases by 5.

**Source:** `= this.source` (`= this.source-type`)
