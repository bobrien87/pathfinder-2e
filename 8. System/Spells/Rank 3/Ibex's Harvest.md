---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]"]
cast: "1 to 3"
range: "varies"
area: "10-foot emanation"
targets: "1 or more creature"
defense: "basic Will"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

In the tale "Ibex's Harvest," Ibex turns from the path of a warrior to the path of a farmer, building up their community by working hard and sharing a bountiful harvest not just with their humanoid neighbors but also with their animal neighbors. Ibex initially focuses on distributing equally among the animals but learns that true equality requires knowing what each being needs. The number of actions you spend when Casting this Spell and telling the story determine its targets and effects.

`pf2:1` You give a brief description of Ibex's first bounty. One willing target you can touch gains 10 temporary Hit Points that last 1 minute.

`pf2:2` You tell the tale of how Ibex shared their harvest equally between Hippo and Ant. Two willing targets within 20 feet each gain 10 temporary Hit Points that last 1 minute.

`pf2:3` You impart Ibex's lesson about how to prevent others from taking advantage of generosity. All creatures within a 10-foot emanation are affected by the tale. Choose one creature in the emanation to take 2d8 mental (basic Will save), while each other creature in the emanation gains 5 temporary Hit Points that last 1 minute.

**Heightened (+1)** The temporary Hit Points increase by 3 and the mental damage for the 3-action version increases by 1d8.

> [!danger] Effect: Spell Effect: Ibex's Harvests

**Source:** `= this.source` (`= this.source-type`)
