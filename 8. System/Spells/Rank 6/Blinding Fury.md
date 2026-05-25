---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Emotion]]", "[[Incapacitation]]", "[[Mental]]"]
cast: "`pf2:r`"
range: "60 feet"
targets: "The triggering creature"
defense: "Will"
duration: "varies"
requirements: "A creature damages you"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature damages you.

You curse the target with your outrage at being attacked. The effect is determined by the target's Will save.
- **Critical Success** The target is unaffected.
- **Success** The target can't [[Observe]] you until the end of its turn, and if you're currently observed by it, you become [[Hidden]] to it.
- **Failure** As success, and for 1 minute, every time the target damages you, it can't observe you until the end of its turn.
- **Critical Failure** As success, and for an unlimited duration, the first time each round the target damages a creature, it can't observe that creature until the end of its turn. If it damages several creatures at once, the creature it can't perceive is chosen randomly among those creatures.

**Source:** `= this.source` (`= this.source-type`)
