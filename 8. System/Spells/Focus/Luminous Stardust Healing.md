---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You scatter twinkling sparks from your sentinel weapon, replenishing your allies' fighting spirit and driving out evil. The target regains 16 Hit Points. If they were affected by a possession effect, you attempt to counteract the effect, casting out the possessing entity on a success and preventing them from possessing the target again for 1 week. If you fail, the entity is immune to being cast out by this spell for 1 week, though you can still heal the target as normal.

**Heightened (+1)** The amount of healing increases by 8.

**Source:** `= this.source` (`= this.source-type`)
