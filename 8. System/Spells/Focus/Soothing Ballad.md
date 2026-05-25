---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Bard]]", "[[Composition]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "you and up to 9 allies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw upon your muse to soothe your allies. Choose one of the following three effects:

- The spell attempts to counteract fear effects on the targets.

- The spell attempts to counteract effects imposing paralysis on the targets.

- The spell restores 7d8 Hit Points to the targets.

**Heightened (+1)** When used to heal, soothing ballad restores 1d8 more Hit Points.

**Source:** `= this.source` (`= this.source-type`)
