---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 110}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Tian Xia origin

Black swill with multicolored ribbons makes this vinegar look like an oil spill.

Ingesting a dose of rainbow vinegar makes your sweat acidic and nonconductive for 10 minutes. During this time, your unarmed attacks deal an additional 1d8 acid damage, and you have resistance 15 to electricity. Vampires find this vinegar particularly harmful and take an additional 2d8 acid damage instead.

> [!danger] Effect: Rainbow Vinegar

Taking more than one dose of rainbow vinegar in a single day gives you weakness 5 to acid until your next daily preparations.

> [!danger] Effect: Rainbow Vinegar Weakness

**Source:** `= this.source` (`= this.source-type`)
