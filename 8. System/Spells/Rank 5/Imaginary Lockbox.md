---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "1 minute"
range: "touch"
targets: "1 container and its contents, totaling 10 Bulk or less"
duration: "until the next time you make your daily preparations"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You turn a container and its contents into an imaginary form stored in your mind that only you can see and interact with. The container's physical properties—the material from which it's made, any locks, or other features—are irrelevant to the casting of this spell, but the container can't contain any creatures. The container has no Bulk, and you can visualize everything inside it.

You can retrieve an item from the lockbox as an activity that takes 3 actions and has the concentrate and manipulate traits. Putting items back isn't possible. You can Dismiss the spell. When the spell ends, the container returns to its normal state, either appearing in your hands if it can fit there or on the ground adjacent to you if not.

**Source:** `= this.source` (`= this.source-type`)
