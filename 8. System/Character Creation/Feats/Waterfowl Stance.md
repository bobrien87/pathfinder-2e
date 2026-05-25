---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Monk]]", "[[Stance]]", "[[Water]]"]
prerequisites: "Monastic Weaponry"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

In your hands, swords dance like rainfall over the waves; who can tell where the storm ends and the sea begins? Developed by Swordmaster Ganhil to compete with the House of Untwisting Iron, this stance integrates fluid swordplay into even the simplest movements.

While in Waterfowl Stance, the dandpatta, scimitar, talwar, and zulfikar gain the monk trait for you. When you [[Tumble Through]] a creature's space or [[Leap]] over a creature while wielding one of these weapons, you can deal that creature 1d6 slashing damage. This damage is increased to 2d6 if the weapon has a greater striking rune and 3d6 if it has a major striking rune.

**Special** You gain access to the dandpatta, talwar, and zulfikar.

**Source:** `= this.source` (`= this.source-type`)
