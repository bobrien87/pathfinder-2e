---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Linguistic]]", "[[Manipulate]]", "[[Mental]]", "[[Sleep]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing creature"
duration: "1 hour"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With your soothing words, you lull the target into an enchanting dream. When you Cast the Spell, the target falls [[Unconscious]] if it wasn't already. While unconscious, it experiences a dream of your choice, though lucidly enough it can wake when it pleases. If it wakes up before 1 minute of sleep has passed, the spell ends.

- **Dream of Insight** +1 status bonus to Intelligence-based skill checks

- **Dream of Glamor** +1 status bonus to Charisma-based skill checks

- **Dream of Voyaging** +5-foot status bonus to Speed

If you Cast this Spell again, any previous *sweet dream* you cast ends.

> [!danger] Effect: Spell Effect: Sweet Dream

**Heightened (4th)** The bonus for a dream of insight or glamor is +2.

**Heightened (7th)** The bonus for a dream of insight or glamor is +3.

**Source:** `= this.source` (`= this.source-type`)
