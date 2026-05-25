---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1800}"
bulk: "4"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tower shield is crafted from interlocking sections of an arctic cave worm's chitin that are rimed with constant frost. It has Hardness 13, HP 104, and BT 52.

**Activate—Misty Chill** `pf2:1` (cold, concentrate, manipulate)

**Effect** You Raise the Shield and an icy mist begins to flow off it. Until the beginning of your next turn, you gain resistance 5 to cold and any creature that ends its turn adjacent to you takes 3d6 cold damage (DC 29 [[Reflex]] save).

> [!danger] Effect: Misty Chill

**Craft Requirements** The initial raw materials must include chitin from an arctic cave worm.

**Source:** `= this.source` (`= this.source-type`)
