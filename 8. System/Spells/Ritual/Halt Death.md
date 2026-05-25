---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "10"
traits: ["[[Vitality]]"]
cast: "8 hours"
area: "5280-foot emanation"
targets: "all living creatures"
duration: "1 day"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

While death may be war's stock and trade, you attempt to momentarily delay the inevitable. Upon the successful completion of the ritual, the sands of the hourglass begin to slowly float upward into the upper bulb over the course of the next 24 hours. The hourglass shatters at the end of the ritual's duration, ending the protective magic.
- **Critical Success** All living creatures within the area are guarded against death, gaining a +4 status bonus to saving throws against death effects. In addition, when a living creature in the area succeeds at a recovery check, they get a critical success instead. Finally, the first time during the duration that a living creature would be reduced to dying 2 or higher, that creature remains at dying 1 instead.
- **Success** All living creatures within the area are guarded against death, gaining a +2 status bonus to saving throws against death effects. In addition, the first time during the duration that a living creature would be reduced to dying 3 or higher, that creature remains at dying 2 instead.
- **Failure** The ritual has no effect.
- **Critical Failure** Attempting to stave off death earns Pharasma's ire. You and all the secondary casters become [[Doomed]] 2. This condition can't be reduced or removed for 1 week.

> [!danger] Effect: Halt Death

**Source:** `= this.source` (`= this.source-type`)
