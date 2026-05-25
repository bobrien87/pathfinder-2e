---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 350}"
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

Arbor wine that has been aged for several years—or artificially aged with alchemy—develops both a greater complexity of flavor and a stronger connection to nature. When you drink aged arbor wine, vegetation in a @Template[type:emanation|distance:20] around you begins to writhe, becoming difficult terrain until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
