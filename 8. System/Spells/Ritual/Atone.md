---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
cast: "1 day"
range: "10 feet"
targets: "another creature of up to 8th level who is a worshipper of the same deity or philosophy as you"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You attempt to help a truly penitent creature atone for its misdeeds, typically actions anathema to your deity. If the creature isn't truly penitent, the outcome is always a critical failure. This ritual uses Nature if the target is a druid, and Religion in all other cases.
- **Critical Success** The creature receives absolution for its misdeeds, allowing it to regain standing with your deity. It regains any abilities it lost. Before the atonement is complete, the creature must perform a special quest or other task chosen by your deity, as befits its misdeeds. If completed during downtime, this task should take no less than 1 month. For 1 month, the target receives divine insight just before performing an act that would be anathema to your deity.
- **Success** As critical success, but the creature gains no special insight regarding its subsequent actions.
- **Failure** The creature does not receive absolution and must continue to meditate and redress its misdeeds. Any future *atone* rituals for the same misdeeds cost half as much and gain a +4 circumstance bonus to primary and secondary checks.
- **Critical Failure** The creature offends your deity and is permanently cast out from the faith. The creature can't rejoin your religion without a more direct intervention.

**Heightened (+1)** Increase the maximum target level by 2 and the base cost by 20 gp.

**Source:** `= this.source` (`= this.source-type`)
