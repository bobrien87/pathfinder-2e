---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing creature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You drive mental contamination from the target's mind. Attempt to counteract an effect of your choice imposing one of these conditions on the target: [[Fleeing]], [[Frightened]], and [[Stupefied]]. If you failed to counteract the effect but you would have if its counteract rank were 2 lower, instead suppress the effect until the beginning of your next turn. The effect's duration doesn't elapse while it's suppressed. This spell can't counteract or suppress conditions that are part of curses, diseases, or a natural state of the target.

**Heightened (4th)** Add [[Confused]], [[Controlled]], and [[Slowed]] to the list of conditions.

**Heightened (6th)** As 4th rank, plus add [[Doomed]].

**Heightened (8th)** As 4th rank, plus add doomed and [[Stunned]].

**Source:** `= this.source` (`= this.source-type`)
