---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Focus]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 creature"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

When you touch the target, a symbol of the moon appears on its forehead, glowing with soft moonlight. The target glows with dim light in a 20-foot radius. It also gets a benefit based on a phase of the moon, starting with the new moon and changing to the next phase at the end of each of its turns.

- **New Moon** The target receives no benefit.

- **Waxing Moon** The target gains a +1 status bonus to attack rolls and a +4 status bonus to damage rolls.

- **Full Moon** The target gains a +1 status bonus to attack rolls, AC, and saves, and a +4 status bonus to damage.

- **Waning Moon** The target gains a +1 status bonus to AC and saving throws. After this phase, return to the new moon.

> [!danger] Effect: Spell Effect: Touch of the Moon

**Source:** `= this.source` (`= this.source-type`)
