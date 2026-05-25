---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Wizard]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "one creature you can see"
defense: "basic Fortitude"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your gaze falls on a creature, filled with icy vengeance or fiery wrath. The gaze deals 1d4 damage (basic Fortitude save). It deals your choice of cold damage or fire damage and gains the appropriate trait. If you already dealt damage to the creature earlier this turn, it also takes 1 persistent damage of the gaze's type (@Damage[(@item.rank)[cold,persistent]]{persistent cold damage} or @Damage[(@item.rank)[fire,persistent]]{persistent fire damage}).

**Heightened (+1)** The initial damage increases by 1d4 and persistent damage by 1.

**Source:** `= this.source` (`= this.source-type`)
