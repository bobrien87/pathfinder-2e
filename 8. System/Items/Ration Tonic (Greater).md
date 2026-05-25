---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
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

**Activate** `pf2:1` (manipulate)

This slender vial appears to hold clean, clear water with a faintly fruity scent. Drinking a ration tonic magically nourishes you with the equivalent of a week's worth of food and water, distributing the nourishment in a constant and healthy flow across the week. The tonic has a subtle, pleasant taste, its particulars chosen when the potion is crafted.

**Source:** `= this.source` (`= this.source-type`)
