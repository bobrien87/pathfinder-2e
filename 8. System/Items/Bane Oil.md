---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 12}"
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

Bane oil comes in as many forms as the bane weapon property rune. Coating a weapon with the oil gives the weapon the benefit of one type of [[Bane]] rune for 1 minute. A weapon can be coated in only one type of bane oil at a time. Any new application of this oil supersedes any previous one. If a weapon has the bane rune, this oil has no effect if it's of the same type as the rune.

**Source:** `= this.source` (`= this.source-type`)
