---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 60}"
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

Using ingredients collected from pure elemental sources, a warding element draught instills enough of the essence of the element in the imbiber to partially protect them against it. Each draught includes one of the following ingredients, chosen when the elixir is distilled, and grants a +1 item bonus to AC and saving throws against alchemical effects, spells, and magic effects with the listed elemental trait for 10 minutes.

- **Blood** Metal
- **Effervescent Gas** Air
- **Grains** Earth
- **Hot Peppers** Fire
- **Spring Water** Water
- **Wormwood** Wood

**Source:** `= this.source` (`= this.source-type`)
