---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:3`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are piloting a vehicle.

(reckless) You try to run over creatures with your vehicle, possibly also ramming one larger creature or object. If you maintain control of your vehicle, the vehicle moves up to twice its Speed in a straight line at the vehicle's current heading. You attempt to run over any creatures in your path two sizes smaller than the vehicle or smaller, and you can attempt to ram one target creature or object in your path one size smaller than the vehicle or larger.

Each creature in your path, including a rammed target, takes the vehicle's collision damage (basic Reflex save at vehicle's collision DC). If the rammed target is a vehicle, its pilot can attempt a piloting check in place of this Reflex save, with the same results. If the target of your ram takes damage, you and your vehicle each take collision damage (no save) and your movement ends.

**Source:** `= this.source` (`= this.source-type`)
