---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Drinking this thick, fortifying potion grants 10 resistance against a single damage type for 1 hour. Each *potion of resistance* is created to defend against acid, cold, electricity, fire, or sonic damage (and is called a *lesser potion of fire resistance* or the like).

**Source:** `= this.source` (`= this.source-type`)
