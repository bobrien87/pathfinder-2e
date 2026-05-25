---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Animist]]", "[[Apparition]]", "[[Concentrate]]", "[[Spellshape]]"]
frequency: "once per PT10M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

Gaining substance from your magic, your apparitions increase the range of your spells, which then pull your enemy closer. If the next action you use is to Cast a Spell that has a range and targets one creature, increase that spell's range by 30 feet. As is standard for increasing spell ranges, if the spell normally has a range of touch, you extend its range to 30 feet. In addition to the normal effects of the spell, your apparitions briefly take on semi-physical forms and attempt to drag the target toward you. The target must attempt a Fortitude saving throw against your spell DC; on a failure, it is pulled up to 30 feet directly toward you.

**Source:** `= this.source` (`= this.source-type`)
