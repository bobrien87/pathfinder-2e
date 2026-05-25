---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]"]
price: "{'gp': 5}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

Life shot is a special cartridge that carries a small dose of elixir of life. A creature hit by activated life shot takes no damage from the successful attack, instead receiving 1d4 healing healing and gaining a +1 item bonus to saving throws against diseases and poisons for 1 minute. On a critical hit, roll the healing received twice and take the better result (this is a fortune effect). A target willing to be hit by this attack is [[Off Guard]] against it.

> [!danger] Effect: Life Shot

**Source:** `= this.source` (`= this.source-type`)
