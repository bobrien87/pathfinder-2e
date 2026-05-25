---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:3`"
range: "touch"
targets: "1 willing creature"
duration: "Until the target's next daily preparations"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You establish a mental link with the target, focusing on a piece of knowledge important to their culture, family (by birth or choice), or home settlement. Both you and the target must be aware this knowledge exists, even if you don't know the exact details.

As your magic connects them to this legacy, the target gains a non-lineage ancestry feat from their ancestry. The feat must be of a level no higher than twice recall legacy's rank and the target must meet any prerequisites for the feat.

The target is then immune to any further castings of recall legacy until their next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
