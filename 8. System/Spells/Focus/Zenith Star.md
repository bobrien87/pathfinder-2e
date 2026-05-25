---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "1 day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call a tiny star to orbit a creature in a sparkling halo before shooting up into the heavens, where it marks the creature's rough location. The target must attempt a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Dazzled]] for 1 round.
- **Failure** The target is dazzled for 1 round. While the spell persists, as long as you can see the night sky and the target is visible from the same night sky, you can sense the approximate direction and distance to the creature by Sustaining the spell. This is enough to track the creature, but not pinpoint their exact square (for instance, to make an attack). You can set a number of zenith stars equal to your Wisdom modifier; if you exceed this number, your oldest zenith star is automatically Dismissed.
- **Critical Failure** As failure, but the target is [[Blinded]] for 1 round.

**Heightened (+1)** The duration increases by 1 day.

**Heightened (4th)** You ignore the [[Concealed]] condition against targets marked by zenith star.

**Source:** `= this.source` (`= this.source-type`)
