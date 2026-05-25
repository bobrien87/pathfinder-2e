---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You sharpen a creature's senses, though more distant objects become hazy, indistinct, or muted to it. The target gains a +1 status bonus to Perception checks attempted with any of its precise senses. Furthermore, any imprecise senses the target has are sharpened to precise senses (though they don't receive the status bonus). However, the target can't perceive anything beyond a range of 20 feet with any of its senses.

The duration is determined by the target's Will save. You can allow allies to choose the outcome instead of attempting a saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target is affected for 1 round.
- **Failure** The target is affected for 1 minute.
- **Critical Failure** As failure, but the target can't perceive anything beyond a range of 10 feet.

**Heightened (3rd)** You can target up to 2 creatures.

**Heightened (6th)** You can target up to 4 creatures.

**Source:** `= this.source` (`= this.source-type`)
