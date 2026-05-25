---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 7500}"
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

A popular choice for investigators studying alchemy, insight coffee is infused with alchemical flavoring during percolation. For 1 hour after you drink an insight coffee, you use d8s instead of d6s for your extra damage from the strategic strike class feature, if you have it. You also gain a +4 item bonus to checks to Recall Knowledge with a skill determined by the blend chosen when the item is crafted.

- **Double Coffee** Religion
- **Hazelnut** Nature
- **Mocha** Arcana
- **Vanilla** Society
- **Pumpkin Spice** Occultism
- **Toffee** Medicine

> [!danger] Effect: Insight Coffee

**Source:** `= this.source` (`= this.source-type`)
