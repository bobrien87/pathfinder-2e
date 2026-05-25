---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Tian Xia origin

This strong, clear liquor is made from fermented rice.

When you drink a cup of iron wine, your sweat becomes highly combustive for the next 10 minutes, igniting with the slightest bit of friction. This causes your unarmed attacks to deal an additional 1d4 fire damage for the duration of the effect.

> [!danger] Effect: Iron Wine

Drinking more than one cup of iron wine in a single day gives you weakness 5 to fire until your next daily preparations.

> [!danger] Effect: Iron Wine Weakness

**Source:** `= this.source` (`= this.source-type`)
