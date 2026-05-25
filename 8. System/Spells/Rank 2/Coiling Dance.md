---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Holy]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You perform a dance that seeks to pass on the knowledge and wisdom of a naga. Your allies in the area are filled with sacred energy, making their spells and attacks holy. Creatures or effects that would be unholy don't gain this benefit

> [!danger] Effect: Spell Effect: Coiling Dance

When you cast or Sustain this spell, you can choose an ally in the area that's [[Grabbed]], [[Immobilized]], or [[Restrained]]. They can immediately use a reaction to [[Escape]]; they can use your Occultism or Religion modifier for the check instead of their unarmed attack, Acrobatics, or Athletics modifier if that would be better.

**Source:** `= this.source` (`= this.source-type`)
