---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
traits: ["[[Earth]]"]
cast: "8 hours"
range: "5 miles"
duration: "1 week"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You spill the ink on an accurate map of the area, which transforms into a series of lines that correspond to a new network of tunnels under the earth. A momentary shift, like the aftershock of a distant earthquake, is the only aboveground sign that anything has occurred. You choose a single entrance and exit to these tunnels, which must be locations within range that are known to you, though you need not be familiar with them. For example, you could name "the basement of the town hall" as an exit if you knew the town hall had a basement but had never seen it with your own eyes. If either named entrance or exit doesn't exist, the ritual fails. The entrance and exit are difficult to spot, requiring a successful DC 35 [[Perception]] check to see; the casters automatically succeed at this check.

The tunnels avoid existing subterranean features and underground structures, unless they're designated as an entrance or an exit. The tunnels are 10 feet wide and 15 feet high, providing room for most armies, but the passageways twist and turn, making navigation difficult. A creature can lead groups through the tunnels with a successful DC 32 [[Survival]] check to Sense Direction. On a success, the group reaches the other end of the tunnels in 2 hours. Failure on this check means the group gets lost within the tunnels for 4 hours, after which the leader can attempt the check again. A critical failure means that the group spends 8 hours wandering through the tunnels, only to arrive where they entered; the leader can attempt the check again the next day.

If any creature is in the tunnels when the ritual's duration ends, it's harmlessly pushed to the nearest entrance or exit.
- **Critical Success** The map provides some indication of the layout of the tunnels. A creature with the map gains a +2 circumstance bonus to the Survival check to navigate the tunnels. Any creatures not allied with the casters take a –2 circumstance penalty to the Perception check to spot the entrance and exit.
- **Success** As critical success, but the bonus to the Survival check is +1, and the penalty to the Perception check is –1.
- **Failure** The ritual has no effect.
- **Critical Failure** The ground beneath your feet rebels against your attempt to control it. The casters are attacked by a pair of elite Elemental Avalanches.

**Source:** `= this.source` (`= this.source-type`)
