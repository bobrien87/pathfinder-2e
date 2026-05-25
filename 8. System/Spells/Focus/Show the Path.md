---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Fortune]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing creature"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grant the target insight on things to come, guiding them toward a fate they find most fitting and encouraging them to continue this journey. The creature rolls a d20 at the start of each of its turns. The creature can use the result of the roll instead of rolling for any check before the start of their next turn. If the creature does substitute the roll in this way, they gain a +1 status bonus to whatever check they substitute on the following turn. Repeated substitutions increase the status bonus by 1, up to a total of +2. If the creature begins their turn without having substituted a roll in the previous round, the spell ends.

**Heightened (7th)** The status bonus can increase up to a total of +3.

**Heightened (10th)** The status bonus can increase up to a total of +4.

**Source:** `= this.source` (`= this.source-type`)
