---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "10 minutes"
range: "20 feet"
targets: "you and up to 5 willing creatures"
duration: "8 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The targets naturally take on animal forms most fitting their movement and environment. Each target gains a land, burrow, climb, fly, and swim Speed of 40 feet, and can transform into a Tiny or Small animal most appropriate for a given movement and environment. It also gains immunity to mild, severe, and extreme cold and heat, along with any other immunities common to the local wildlife, at the GM's discretion. In exploration mode, a target can move much faster, at a travel Speed of 20 miles per hour.

A target can't Strike, cast spells, or use most manipulate actions in animal form, but it can resume its normal shape by Sustaining the spell. It can Sustain the spell again to resume animal form.

**Source:** `= this.source` (`= this.source-type`)
