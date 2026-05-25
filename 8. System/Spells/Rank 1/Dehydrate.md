---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You stir the inner fire of all things within the area, driving out moisture. All creatures in the area take 1d6 persistent fire damage with a basic Fortitude save; creatures with the water or plant traits get a result one degree of success worse than they rolled. The spell ends for a creature when its persistent damage ends.

A creature affected by *dehydrate* attempts an additional Fortitude save at the end of each of its turns, before rolling to recover from the persistent damage. It can forgo this additional save if it consumed water or a similar hydrating liquid within the last round (drinking typically requires a single action).
- **Success** The creature takes no additional effect.
- **Failure** The creature is [[Enfeebled]] 1 until the end of its next turn.
- **Critical Failure** The creature is [[Enfeebled]] 2 until the end of its next turn.

**Heightened (+2)** The range increases by 10 feet, the burst increases by 5 feet, and the persistent fire damage increases by 3d6.

**Source:** `= this.source` (`= this.source-type`)
