---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 130}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Watering grape or berry bushes with certain alchemical liquids as they grow results in a ruby-red drink that's rich and heady. The vines develop a connection to their natural environment and impart it onto the wine's imbiber. For 1 minute after drinking a glass of arbor wine, you have tremorsense at a range of 30 feet.

> [!danger] Effect: Arbor Wine

**Source:** `= this.source` (`= this.source-type`)
