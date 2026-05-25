---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Scrying]]"]
cast: "10 minutes"
range: "planetary"
targets: "1 creature"
defense: "Will"
duration: "10 minutes (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You magically spy on a creature of your choice. *Scrying* works like [[Clairvoyance]], except that the image you receive is less precise, insufficient for *teleport* and similar spells. Instead of creating an eye in a set location within 500 feet, you instead create an eye that manifests just above the target. You can choose a target either by name or by touching one of its possessions or a piece of its body. If you haven't met the target in person, *scrying*'s DC is 2 lower, and if you are unaware of the target's identity (perhaps because you found an unknown creature's fang at a crime scene), the DC is instead 10 lower.

The effect of *scrying* depends on the target's Will save.
- **Critical Success** The spell fails and the target is temporarily immune for 1 week. The target also gains a glimpse of you and learns its rough distance and direction from you.
- **Success** The spell fails and the target is temporarily immune for 1 day.
- **Failure** The spell succeeds.
- **Critical Failure** The spell succeeds, and the eye follows the target if it moves, traveling up to 60 feet per round.

**Source:** `= this.source` (`= this.source-type`)
