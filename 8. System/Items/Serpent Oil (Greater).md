---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 56}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This glistening oil has a green hue and tiny snake scales floating within. If you slather serpent oil on a Medium object that is snakelike in shape, from a stick to a scarf, the object transforms into a [[Giant Viper]], keeping some of the same colors and patterns of the original item. If placed on other objects, the oil fails and is wasted. This false snake has the minion trait. It remains in snake form for 1 minute before returning to its object state. If slain, the item returns to its original form, unharmed.

**Source:** `= this.source` (`= this.source-type`)
