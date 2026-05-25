---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Wizard]]"]
cast: "`pf2:1`"
range: "60 feet"
targets: "1 willing creature"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You exert magical force to propel a willing creature up to 10 feet in a straight line, including upward, though if they aren't on solid ground or have another way to maintain their height (such as a fly Speed) when the movement ends, they fall. When you Sustain the spell, you can move them again or choose a new target within range and move them instead.

You can cast this spell on an [[Unconscious]] ally, and if you do, the movement from this spell doesn't trigger reactions.

**Heightened (4th)** The distance increases to 20 feet.

**Heightened (7th)** The distance increases to 30 feet.

**Source:** `= this.source` (`= this.source-type`)
