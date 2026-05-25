---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "60-foot line"
defense: "Fortitude"
duration: "until the start of your next turn"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A violent wind issues forth from your palm, blowing from the point where you are when you Cast the Spell to the line's opposite end. The wind extinguishes small non-magical fires, disperses fog and mist, blows objects of light Bulk or less around, and pushes larger objects. Large or smaller creatures in the area must attempt a Fortitude save. Large or smaller creatures that later move into the gust must attempt the save on entering.
- **Critical Success** The creature is unaffected.
- **Success** The creature can't move against the wind.
- **Failure** The creature is knocked [[Prone]]. If it was flying, it takes the effects of critical failure instead.
- **Critical Failure** The creature is pushed 30 feet in the wind's direction, knocked prone, and takes 2d6 bludgeoning damage.

**Source:** `= this.source` (`= this.source-type`)
