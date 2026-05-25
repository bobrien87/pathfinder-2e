---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shroud a creature from others' senses. The target becomes [[Invisible]], but not merely to vision. The invisibility granted by *disappearance* applies to all precise senses an observer might have. It's still possible for a creature to find the target by Seeking using various senses, looking for disturbed dust, hearing gaps in the sound spectrum, or finding some other way to discover the presence of a creature that is otherwise undetectable.

**Source:** `= this.source` (`= this.source-type`)
