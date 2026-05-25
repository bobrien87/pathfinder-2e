---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "unlimited"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You alter the target's memories by erasing a memory, enhancing a memory's clarity, altering a memory, or adding a false memory. The target can attempt a Will save to resist the spell.
- **Critical Success** The target is unaffected and realizes you tried to alter its memory.
- **Success** The target is unaffected but thinks your spell was something harmless instead of *rewrite memory*, unless it identifies the spell.
- **Failure** During the first 5 minutes of the spell's duration, you can Sustain the spell to modify a memory once each round. When you do, you imagine up to 6 seconds of memory to modify, to a maximum of 5 continuous minutes of memory.

Any memories you've altered remain changed as long as the spell is active. If the target moves out of range before the 5 minutes is up, you can't alter any further memories.

**Heightened (6th)** You can Cast the Spell on a willing target to suppress all memory of a particular topic, detailed in 50 words or fewer. The effect is permanent, and it patches these omissions with an indistinct haze.

**Source:** `= this.source` (`= this.source-type`)
