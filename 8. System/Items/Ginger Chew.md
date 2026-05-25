---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 28}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This chewy ginger candy aids digestion and soothes unsettled stomachs. A ginger chew lasts for 1 hour and grants you a +1 item bonus to Fortitude saves against being sickened.

> [!danger] Effect: Ginger Chew

**Secondary Effect** `pf2:1`

**Effect** Reduce your sickened value by 1, if any. The chew becomes inert.

**Source:** `= this.source` (`= this.source-type`)
