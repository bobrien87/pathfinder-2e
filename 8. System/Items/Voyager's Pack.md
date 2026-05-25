---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Extradimensional]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 14800}"
usage: "wornbackpack"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather rucksack has icons burned into it, and every time it's taken to a plane it hasn't been to before, a new icon representing that plane scorches into the surface.

The pack grants you a +3 bonus to Survival checks.

It also enables you to see the magical traces of creatures' passage, allowing you to Track a creature that has teleported. The GM sets the DC of this check, usually using the level and DC of the teleportation spell. This lets you find the location of the creature's destination, and you can use that destination when casting [[Teleport]] or activating the pack, even though you don't know what it looks like.

The pack contains an extradimensional space with the same properties as a *[[Spacious Pouch (Type II)]]*.

This space contains the contents of a climber's kit. If any components of that kit are removed and not returned, they return to the pack at dawn each day.

**Activate—Group Voyage** 10 minutes (concentrate, manipulate)

**Effect** As you activate the pack, you can harness up to four willing creatures to the ropes on the pack. At the end of the activation time, the pack casts a 7th-rank [[Interplanar Teleport]] or [[Teleport]] spell, transporting you and everyone attached to the pack. Attempt a DC 45 [[Survival]] check. On a success, you arrive 25 miles off target using *interplanar teleport* or halve the distance you're off-target with *teleport*. On a critical success, you arrive exactly on target

**Source:** `= this.source` (`= this.source-type`)
