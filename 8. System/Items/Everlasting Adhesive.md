---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (manipulate)

This peculiar amber adhesive bonds two surfaces together almost inseparably. A single flask covers an area up to 1 square foot and must be used all at once to form a single bond between two surfaces. If the activation is interrupted, the bond fails, and the adhesive is wasted.

Once two surfaces are joined with everlasting adhesive, a creature can separate them only with a successful DC 50 [[Athletics]] check. The adhered objects tend to break before the adhesive does unless they're particularly durable, though a creature determined to separate the objects can break off the parts connected by the everlasting adhesive and later Repair the objects.

The adhesive can affect creatures only if they're willing, and its bond can be broken by exfoliating the outermost layer of skin.

**Source:** `= this.source` (`= this.source-type`)
