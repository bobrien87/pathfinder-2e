---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "30-foot cylinder"
defense: "Fortitude"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 60-foot tall, 30-foot radius cylinder

Extraordinary telekinetic pressure smashes down through the area, battering creatures within it to the ground. All flying creatures in the area descend to the bottom of the spell's area, taking twice as much bludgeoning damage as if they had fallen the distance moved, to a maximum of 60 falling damage if they fall 60 feet. They take this falling damage even if the spell's area is entirely in the air and they don't hit the ground, as they concuss against the bottom of the spell's area at great speed. Creatures on the ground and within the spell's area, including flying creatures forced to the ground, must attempt Fortitude saves.
- **Critical Success** The creature is unaffected, and if it was flying, it isn't knocked [[Prone]] even though it took falling damage.
- **Success** The creature is knocked prone.
- **Failure** The creature is knocked prone and [[Stunned]] 2.
- **Critical Failure** The creature is knocked prone and stunned for 1 round.

**Source:** `= this.source` (`= this.source-type`)
