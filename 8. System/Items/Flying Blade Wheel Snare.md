---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 10000}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a creature enters the square, a deadly flying wheel of spinning blades launches at it, making a Strike with an attack modifier of +35 and dealing 8d8 slashing damage. Once on each of your turns, you can use an Interact action within 120 feet of the wheel to cause it to Fly up to 60 feet toward the creature it's chasing and make another Strike if it's within 5 feet of its target after it moves. After 1 minute, the spinning ceases and the wheel falls to the ground. Creatures can destroy the wheel to stop it (AC 37, Fort +29, Ref +20, HP 200, Hardness 10, object immunities).

**Source:** `= this.source` (`= this.source-type`)
