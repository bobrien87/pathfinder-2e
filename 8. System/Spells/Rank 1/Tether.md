---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You use magical chains, vines, or other tethers to bind your target to you. The creature can still try to [[Escape]], and it or others can break the tethers by attacking them (the tethers have AC 15 and 10 Hit Points). You must stay within 30 feet of the target while it's tethered; moving more than 30 feet away from your target ends the spell. The target must attempt a Reflex save. You can Dismiss the spell.
- **Critical Success** The target is unaffected.
- **Success** The target takes a –5-foot circumstance penalty to its Speed as long as it's within 30 feet of you.
- **Failure** The target takes a –10-foot circumstance penalty to its Speed and can't move more than 30 feet away from you until it Escapes or the spell ends.
- **Critical Failure** The target is [[Immobilized]] until it Escapes or the spell ends.

**Heightened (+1)** The tethers' AC increases by 3, and their Hit Points increase by 10.

**Source:** `= this.source` (`= this.source-type`)
