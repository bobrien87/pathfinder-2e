---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grow a set of colored, glowing scales or scaled armor that stores energy before releasing it in a final burst. When you cast this spell, choose acid, cold, fire, electricity, or poison damage. You gain resistance 5 against that type of damage. The scales' color depends on the damage type you chose, such as red or orange for fire damage.

The scales store up energy as they protect you. Keep track of how much damage the scales have prevented. As a 2-action activity that has the concentrate and manipulate traits, you can explode your scales outward in a @Template[type:emanation|distance:20], dealing 1d6 damage of the chosen type to all creatures in the area for every 10 damage the scales have prevented, to a maximum of 10d6 damage (after preventing 100 damage). Each creature in the area must attempt a basic Reflex save. Once you do so, the spell ends.

**Heightened (+2)** The resistance increases by 5, and the maximum damage from the scale explosion increases by 5d6.

**Source:** `= this.source` (`= this.source-type`)
