---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 hour"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

To the target, your words are honey and your visage seems bathed in a dreamy haze. It must attempt a Will save, with a +4 circumstance bonus if you or your allies recently threatened it or used hostile actions against it.

You can Dismiss the spell. If you use hostile actions against the target, the spell ends. When the spell ends, the target doesn't necessarily realize it was charmed unless its friendship with you or the actions you convinced it to take clash with its expectations, meaning you could potentially convince the target to continue being your friend via mundane means.
- **Critical Success** The target is unaffected and aware you tried to charm it.
- **Success** The target is unaffected but thinks your spell was something harmless instead of charm, unless it identifies the spell.
- **Failure** The target's attitude becomes [[Friendly]] toward you. If it was Friendly, it becomes [[Helpful]]. It can't use hostile actions against you.
- **Critical Failure** The target's attitude becomes Helpful toward you, and it can't use hostile actions against you.

**Heightened (4th)** The duration lasts until the next time you make your daily preparations.

**Heightened (8th)** The duration lasts until the next time you make your daily preparations, and you can target up to 10 creatures.

**Source:** `= this.source` (`= this.source-type`)
