---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 1200}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

Wiry designs mark the silvery coating on a garrote shot. When the activated ammunition hits a target, it transforms into a silvery garrote that wraps around one of the target's appendages, dealing 2d12 persistent,slashing. On a critical hit, it wraps around the target's throat if it has one, and the target can't breathe until the persistent damage ends. If the persistent damage kills the target, the garrote severs the appendage it's wrapped around.

**Source:** `= this.source` (`= this.source-type`)
