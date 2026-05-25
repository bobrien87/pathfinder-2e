---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Acid]]", "[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 350}"
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

Ooze ammunition is a capsule containing a sticky substance. If you hit a creature with activated ooze ammunition, it deals acid damage instead of its normal damage type, and the creature then takes a –10-foot penalty to Speed and 3d4 persistent,acid damage until it ends the effects. On a critical hit, the creature is [[Immobilized]] for 1 round in addition to the other effects. The target can end the effects by [[Escaping]] (DC 29) the sticky foam. Other creatures can provide the action, although doing so deals half the ammunition's persistent acid damage to the assisting creature. A creature that ends the effect still takes the persistent damage that turn.

> [!danger] Effect: Ooze Ammunition

**Source:** `= this.source` (`= this.source-type`)
