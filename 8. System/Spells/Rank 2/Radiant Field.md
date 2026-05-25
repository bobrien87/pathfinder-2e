---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an area of bright light. Creatures with [[Light Blindness]] that are [[Blinded]] by *radiant field* and remain in the area must attempt a Fortitude save at the start of their turns. On a failure, a creature remains blinded for 1 round; this is an incapacitation effect.

This spell also suppresses magical darkness of your *radiant field* spell's rank or lower.

**Heightened (4th)** Creatures seen through the area are [[Concealed]] to creatures outside the area. Creatures with light blindness can continue to be blinded by the field as long as the field is visible, even when outside of the field.

**Source:** `= this.source` (`= this.source-type`)
