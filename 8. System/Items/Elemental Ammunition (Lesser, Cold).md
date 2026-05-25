---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Cold]]", "[[Consumable]]", "[[Splash]]"]
price: "{'gp': 3}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

When activated, the reservoir of alchemical reagents in elemental ammunition atomizes on impact, dealing 1 persistent cold damage to the target and 1 splash cold damage in addition to the damage the attack normally deals. Each damage type requires a different formula, and the ammunition gains a trait matching the damage type.

**Source:** `= this.source` (`= this.source-type`)
