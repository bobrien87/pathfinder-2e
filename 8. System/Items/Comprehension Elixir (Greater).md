---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mental]]"]
price: "{'gp': 54}"
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

This bitter draught opens your mind to the potential of the written word. For the listed duration after drinking this elixir, you can understand any words you read, so long as they are written in a common language. This elixir doesn't automatically allow you to understand codes or extremely esoteric passages-you still need to attempt a skill check to Decipher Writing. The duration is 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
