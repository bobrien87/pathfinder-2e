---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Red Mantis Assassin|Red Mantis Assassin]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in sawtooth sabres, deity is Achaekek, member of the Red Mantis assassins"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Mediogalti Island.

You have learned how to stalk your foes and slay them with a sawtooth saber. You become trained in Stealth and Assassin Lore; if you were already trained, you become an expert instead. Whenever your proficiency in any weapon increases to expert or beyond, you also gain that new proficiency with sawtooth sabers.

You become bound by Achaekek's anathema and can receive his sanctification.

Red Mantis Assassin

**Source:** `= this.source` (`= this.source-type`)
