---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You speak on the virtue of charity, compelling the target to give away its possessions. The target must attempt a Will save. If the target has no items on its person, the spell fails.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stunned]] 1 as it wrestles with the urge.
- **Failure** On its next turn, before it does anything else, the target must present the nearest creature with an item in its possession; the target chooses which item to give, and if the only item it has is one that it's currently using to defend itself, such as a weapon during a combat encounter, it can choose to be stunned for 1 round instead of giving up the item. This might require the target to Interact to retrieve an item or move to reach the nearest creature, and passing the item off requires an Interact action as normal.
- **Critical Failure** As failure, except the duration is 4 rounds, and the target must repeat the effects of a failure on each of its turns. At the end of each of its turns, the target can attempt a new Will save to reduce the remaining duration by 1 round, ending the effects entirely on a critical success.

**Source:** `= this.source` (`= this.source-type`)
