---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You open the target's eyes to the plethora of spirits surrounding it—and it sees all these spirits as menacing and powerful. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target believes every spirit it sees is an imminent threat. It's [[Stupefied 3]] for 1 round.
- **Failure** As success, but the effect lasts 1 minute.
- **Critical Failure** As failure, and the target becomes [[Confused]] for 1 round.

**Heightened (6th)** You can target up to 5 creatures.

**Source:** `= this.source` (`= this.source-type`)
