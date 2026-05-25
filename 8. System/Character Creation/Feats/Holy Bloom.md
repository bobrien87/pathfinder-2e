---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rose Warden|Rose Warden]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Rose Warden Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Though you might not be a priest of Milani, her divine spirit flows through you. You gain holy sanctification. Select the freedom or zeal domain. You gain the initial domain spell for that domain. If you don't have one, you gain a focus pool of 1 Focus Point. You can Refocus by praying to Milani or by working with others to plan a just uprising. You become trained in spell attack modifier and spell DC, and your spellcasting attribute for these spells is Wisdom.

**Special** You can choose this feat a second time, gaining the initial domain spell of the domain you didn't gain the first time.

**Source:** `= this.source` (`= this.source-type`)
