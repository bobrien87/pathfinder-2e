---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Mythic]]"]
price: "{'gp': 1000}"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *shield of snakes* (Hardness 10, HP 90, BT 45) is built to resemble a withering tangle of snakes. These serpents slither and hiss whenever you Raise the Shield.

**Activate—Snap Up** `pf2:r`

**Trigger** You roll initiative

**Effect** The *shield of snakes* moves into position, allowing you to Raise the Shield.

**Activate—Snakebite** `pf2:2` (attack)

**Effect** You thrust one of the snake heads at a target, attempting a shield spikes Strike. If you spend 1 Mythic Point, you attempt this Strike at mythic proficiency. On a hit, you inflict damage normally, and then the snakes poison the target, inflicting an additional 2d6 poison damage (DC 27 [[Fortitude]] save).

**Source:** `= this.source` (`= this.source-type`)
