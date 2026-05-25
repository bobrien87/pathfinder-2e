---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 45}"
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

Hot tea with a comforting, flowery aroma, a soothing toddy grants you a +1 item bonus to saving throws against emotion effects and against effects with a trait determined by the liquor mixed into the tea when it's created. These benefits last for 1 hour.

- **Amaretto** Auditory
- **Limoncello** Olfactory
- **Whiskey** Visual

> [!danger] Effect: Soothing Toddy

**Source:** `= this.source` (`= this.source-type`)
