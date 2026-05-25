---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Force]]"]
cast: "1 to 3"
range: "varies"
targets: "1 or more creatures"
defense: "Fortitude"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Gathering kinetic energy, you either focus it in a straight line or disperse it as an encircling ripple. Any creature targeted by this spell must succeed at a Fortitude saving throw or be pushed 10 feet away from you (or 20 feet on a critical failure).

The spell's area or range and how many creatures it affects is based on how many actions you spend when Casting the Spell.

`pf2:1` The spell targets one creature within 15 feet.

`pf2:2` The spell targets one creature within 30 feet. The distance the target is pushed if it fails is doubled, and on a critical failure, the target is also knocked [[Prone]] and takes 1d6 bludgeoning damage.

`pf2:3` The spell targets all creatures in a @Template[emanation|distance:5].

**Source:** `= this.source` (`= this.source-type`)
