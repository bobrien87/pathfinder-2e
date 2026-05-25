---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Aura]]", "[[Concentrate]]", "[[Death]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "5-foot emanation"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth a ghostly lantern that guides the living toward death and the undead toward true death. It sheds bright light in the spell's area and dim light to twice that area. The lantern is insubstantial and floats near you, suspended from an ephemeral, skeletal hand. Living creatures and undead in the area when you Cast the Spell, or that enter the area later, must attempt Fortitude saves. Living creatures that fail their Fortitude saves gain only half the normal benefit from healing effects while within the area. Undead targets that fail their Fortitude saves become [[Enfeebled]] 1 while within the area. Once a creature attempts a save against reaper's lantern, it uses the same outcome if it leaves the area and enters it again.

Once per turn, starting on the round after you cast reaper's lantern, you can Sustain the spell to increase the emanation's radius by 5 feet. When you do so, you force creatures in the area that haven't yet attempted a save against reaper's lantern to attempt one.

**Source:** `= this.source` (`= this.source-type`)
