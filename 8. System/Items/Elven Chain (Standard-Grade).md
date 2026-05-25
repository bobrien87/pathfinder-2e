---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Flexible]]"]
price: "{'gp': 740}"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Elven chain is a [[Chain Shirt]] made of dawnsilver that glitters in even the faintest light. Because it's constructed with small, supple rings, it has no check penalty.

Created by elven artisans employing ancient crafting techniques, elven chain is exceptionally quiet. Unlike other chain shirts-even other dawnsilver chain shirts-elven chain does not have the noisy trait. This suit of armor can be etched with runes like any other dawnsilver chain shirt.

**Craft Requirements** The initial raw materials must include dawnsilver worth at least 3,125 sp.

**Source:** `= this.source` (`= this.source-type`)
