---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Emotion]]", "[[Fear]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Visual]]", "[[Wizard]]"]
cast: "`pf2:1`"
defense: "Will"
duration: "until the beginning of your next turn"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You hold up any object, which takes on the appearance of glowing regalia in the eyes of those who look on you, representing the political or religious institute most feared by each creature. If a creature attempts to attack you during the spell's duration, it must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature becomes [[Frightened]] 1, the penalty applying to its attack roll.
- **Failure** As success, but [[Frightened]] 2.

**Source:** `= this.source` (`= this.source-type`)
