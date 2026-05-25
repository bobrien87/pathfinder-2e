---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
defense: "Will"
duration: "until the end of your next turn"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon an unstoppable stampede of panicking beasts. Whether you conjure wild beasts or tamed cattle, the stampede is a force of nature that leaves behind nothing in its wake. The stampede occupies the space of a Gargantuan creature and has a Speed of 60 feet.

**Arrive**(emotion, fear, mental) *Foreboding Tremors* The sheer energy of a stampede can cause even apex predators to panic. Each creature within a @Template[emanation|distance:60] must attempt a Will save with the following effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 3 and [[Fleeing]] for 1 round.

**Depart***Flatten the Earth* The stampede Strides up to double its Speed, trampling each Large or smaller creature, hazard, and structure whose space it enters, dealing @Damage[(8d8)[bludgeoning]] damage (basic Reflex save). The stampede ignores and attempts to counteract all difficult terrain it enters caused by debris, overgrowth, rubble, or thick ground cover.

**Source:** `= this.source` (`= this.source-type`)
