---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Ghost-Path Epiphany"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Tian Xia's shining cities belie its empires' long shadow of death, darkened by thousands of years of suffering and injustice. You pursue immortality not through tuft-hunting with Heaven's dragons or their imperial brats; yours is the power to crack its corrupt wheel, for you can now release the ghost gates to expedite the dead's revenge at being cheated of their fates.

You cease aging and, regardless of your actual existential state, now register as an undead to effects that can detect undead (such as lifesense or spiritsense).

In addition, you learn [[Create Undead]] rituals for [[Gashadokuro]], Jiang-shi, and [[Shui Gui]]. On a success with one of these rituals, you gain the effects of a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
