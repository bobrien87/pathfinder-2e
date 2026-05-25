---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:3`"
range: "1-mile burst"
defense: "Will"
duration: "until your next daily preparations"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You let loose a primal howl that incites animals and beasts to join in the chorus. Doing so gives you a general idea of how many creatures with the animal or beast trait are within the range of the spell, but significant creatures can attempt a Will save against your spell DC to resist responding to your call. You gain a +1 status bonus to your next Initiative roll in an encounter with an enemy creature that replies to your call. For purposes of using [[Coerce]] during exploration mode, you can communicate with a creature that responds to your call for the duration of the spell. You can only make simple commands, such as approach or hide, and only understand simple ideas, such as compliance with the order or the presence of natural hazards.

**Heightened (+2)** The status bonus increases by 1.

**Source:** `= this.source` (`= this.source-type`)
