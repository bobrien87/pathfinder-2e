---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Oracle]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a surge of healing energy, you push back against an affliction threatening the target and grant a small amount of healing. The target recovers 3d8 Hit Points.

You attempt to counteract any one affliction you are aware the target has, suspending its effects for 1 hour on a success rather than removing it.

The target is then temporarily immune to delay affliction for 1 day. You don't need to have identified the name of the specific affliction, but you do need to be aware of it; for instance, you couldn't delay an ingested poison during its onset period unless you were aware of the poison

**Heightened (+1)** The target recovers an additional 1d8 Hit Points, and you can attempt to suspend an additional affliction

**Source:** `= this.source` (`= this.source-type`)
