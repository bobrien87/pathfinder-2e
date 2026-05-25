---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Focus]]"]
cast: "`pf2:1`"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your apparition guides your attacks and imparts its skill to your movements. For the duration, your proficiency with martial weapons is equal to your proficiency with simple weapons, you gain a +1 status bonus to attack and damage rolls made with weapons or unarmed attacks, and you gain the [[Reactive Strike]] reaction; this reaction gains the apparition trait. The instincts of an apparition of battle run contrary to the use of magic; for the duration of this spell, you take a –2 status penalty to your spell attack modifiers and your spell DCs.

> [!danger] Effect: Spell Effect: Embodiment of Battle

**Heightened (4th)** The status bonus to attack and damage rolls granted by this spell is increased to +2.

**Heightened (7th)** The status bonus to attack and damage rolls granted by this spell is increased to +3.

**Source:** `= this.source` (`= this.source-type`)
