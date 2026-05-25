---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shape energy into a small group of tiny dragons (or other serpentine creatures) that flit around you. Choose fire, force, mental, or spirit damage when you Cast the Spell. For the duration of the spell, your Strikes with weapons or unarmed attacks deal 1 additional damage of the chosen type, as the dragons add their energy to your attacks. You can Sustain the spell to change the damage type.

> [!danger] Effect: Spell Effect: Draconic Barrage

In addition, you can Sustain the spell to have the dragons fly off to bombard a creature within 60 feet. That creature takes 2d4 damage of the chosen type (basic Reflex save). Once the dragons have been used in this way, they wink out of existence and the spell ends.

**Heightened (+1)** The additional amount of damage from the dragons increases by 1 and the damage dealt by the dragons' bombardment increases by 2d4.

**Source:** `= this.source` (`= this.source-type`)
