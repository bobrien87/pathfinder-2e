---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

When created, this mutagen is attuned to one of four energy types: acid, cold, electricity, or fire. When consumed, the mutagen suffuses your body with energy that spills out whenever you attack. At higher levels, it can even grant you the ability to unleash the energy in controlled bursts.

**Benefit** You gain resistance 5 to the attuned energy type. Whenever you score a hit with a melee weapon, add 1 damage of the attuned energy type.

**Drawback** You gain weakness 5 to the other three energy types.

**Duration** 1 minute.

> [!danger] Effect: Energy Mutagen (Lesser)

**Source:** `= this.source` (`= this.source-type`)
