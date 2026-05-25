---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:3`"
range: "500 feet"
area: "30-foot burst"
defense: "basic Will"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

An illusion of horrific creatures fills the spell's area. The creatures look like Tiny swarming monsters with a specific appearance of your choice, such as fiendish flies or animated saw blades. The burst deals 8d8 mental damage with a basic Will save to each creature that's inside the burst when it's created, enters the burst, or starts its turn inside the burst. A creature that critically succeeds at its Will save can immediately attempt to disbelieve the illusion. A creature that tries to Interact with the monsters or observes one with a [[Seek]] action can attempt to disbelieve the illusion. Creatures that disbelieve the illusion take no damage from the illusion thereafter.

**Heightened (+1)** The mental damage increases by 1d8

**Source:** `= this.source` (`= this.source-type`)
