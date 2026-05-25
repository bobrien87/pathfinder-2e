---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 220}"
usage: "wornbelt"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Different versions of the bellflower toolbelt are customized to appear to suit specific trades, so a belt used for carpentry would look different from a belt for baking.

**Activate** `pf2:2` (concentrate, manipulate)

**Effect** You place an object of up to 1 Bulk into the belt, transforming that object into a tool befitting the trade for which the belt was created. Each object remains transformed until it has been removed from the belt for 24 hours or someone uses a single Interact action to return it to its normal form. If enough transformed items are in it, the belt can be used as an [[Artisan's Toolkit]] for that trade.

**Source:** `= this.source` (`= this.source-type`)
