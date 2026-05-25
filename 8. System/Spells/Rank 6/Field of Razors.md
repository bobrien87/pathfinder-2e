---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:3`"
range: "60 feet"
area: "20-foot burst"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grind a chunk of your choice of metal to fine dust between your hands and blow it into the air, where it grows into a tangle of wires covered in razor-sharp prongs. The metal must be of a type you currently have in your possession. The covered area is difficult terrain. A creature that moves through the area takes 5 slashing damage per square traversed.

If a creature takes slashing, piercing, or persistent bleed damage while inside the thicket, you can spend a reaction to grow the iron in the shed blood into additional wires, expanding the burst by 5 feet. You can grow the area four times in this way, to a maximum of a @Template[burst|distance:40].

The barbed wires are made of the metal you chose and activate resistances, weaknesses, and the like normally. The metal reforms in your possession when the spell ends.

**Heightened (+1)** The damage per square increases by 2.

**Source:** `= this.source` (`= this.source-type`)
