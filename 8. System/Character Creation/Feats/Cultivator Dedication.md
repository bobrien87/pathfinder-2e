---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through an esoteric, often exacting, regimen of meditation, diet, and exercise, you've learned to transform your body's inner workings into a crucible of planar and spiritual energies. These austerities allow you to refine your body's vitality into qi, the foundation of all cultivation.

You become an expert in Occultism. In addition, you gain the [[Adapt Self]] domain spell as a focus spell. It costs 1 Focus Point to cast a focus spell, and you start with a focus pool of 1 Focus Point. You refill your focus pool during your daily preparations, and you can regain 1 Focus Point by spending 10 minutes using the Refocus activity meditating to refine essence into qi, which circulates and refills your focus pool. Your cultivator focus spells are occult spells. You're trained in spell attack modifier and spell DC. Your key spellcasting attribute for these spells is Wisdom.

Cultivator focus spells are treated as qi spells for prerequisites, counting the number of qi spells you possess and their effects, such as a jiang-shi's Drain Qi.

Cultivator

**Source:** `= this.source` (`= this.source-type`)
