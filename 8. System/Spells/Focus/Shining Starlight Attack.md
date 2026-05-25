---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** varies (see below)

You brandish your sentinel weapon, summoning the image of your constellation above your head. The constellation then releases a powerful blast that deals 2d10 damage to all enemies in either a @Template[type:line|distance:30] or @Template[type:cone|distance:15], with a basic save against your arcane spell DC. Enemies that critically fail are [[Dazzled]] until the start of your next turn. The damage type, traits, area, and saving throw are determined by your zodiac constellation (see below).

**Heightened (+1)** The damage increases by 1d10.

ConstellationAttack (Area, Save, Damage Type; Traits)Underworld DragonVolcanic vents (line, Reflex, fire)OgreWild club swing (cone, Fortitude, bludgeoning)SwordswomanFalling blades of light (line, Reflex, piercing)Forest DragonSwarm of insects (cone, Fortitude, poison)Sea DragonPressurized seawater (line, Reflex, piercing; water trait)BlossomStorming petals and pollen (line, Fortitude; poison, plant, wood)SwallowWing gust (cone, Reflex, slashing; air)DogA biting dog (line, Reflex, slashing)OxA trampling ox (line, Reflex, bludgeoning)Sky DragonDraconic lightning (line, Reflex, electricity)Sovereign DragonPsychic roar (cone, Will, mental)ArcherHail of silver arrows (piercing, cone, Reflex)

**Source:** `= this.source` (`= this.source-type`)
