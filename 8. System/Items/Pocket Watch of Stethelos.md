---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This brass pocket watch has an unusually complex winding mechanism, and the name inscribed on the back, as well as the numbers on the face, are written in a language no one can identify. Repeated use of the pocket watch attracts the attention of terrible creatures of the Dimension of Time.

**Activate—Steal a Second** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You manipulate time around an ally within 30 feet, allowing them to perceive time differently for a moment. The target is [[Quickened]] for 1 round and can use the action only to Step or Stride.

**Activate—Step Between the Ticks** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You gain 3 actions, each of which must be immediately used to [[Leap]], [[Stand]], [[Step]], or [[Stride]]. If you have an appropriate Speed, you can add Burrow, Climb, Fly, or Swim to this list. While you take these actions, time pauses. All other creatures are completely unaware of your actions, can't speak, and can't use any actions that would be triggered by your movements. While you're taking these actions, you can't take any other actions, including any that would be triggered by the move actions. Once the actions are complete, time starts again, and to onlookers, you seem to have suddenly teleported across the distance you traveled.

**Source:** `= this.source` (`= this.source-type`)
