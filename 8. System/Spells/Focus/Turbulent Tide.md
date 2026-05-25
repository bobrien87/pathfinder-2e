---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Magus]]", "[[Water]]"]
cast: "`pf2:1`"
defense: "Fortitude"
requirements: "You're wielding an improvised weapon."
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause the sheath of water and the improvised weapon it surrounds to surge outward with stupendous force as you attack. Make a melee Strike with your improvised weapon. The weapon then breaks, and each creature adjacent to you must succeed at a Fortitude saving throw against your spell DC or be pushed 5 feet away from you (10 feet on a critical failure). You can Stride after the target of your Strike if they are pushed but you must move the same distance and in the same direction.

If the item has a Hardness greater than your level, or if it's an artifact, cursed item, or other item that's difficult to break or destroy, it doesn't break and adjacent creatures don't need to attempt Fortitude saves.

**Source:** `= this.source` (`= this.source-type`)
