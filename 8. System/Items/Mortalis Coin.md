---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 20}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You are reduced to 0 Hit Points by damage but not immediately killed

**Requirements** You are an expert in Fortitude saves.

This small golden coin is usually stamped with the image of a boar or other resilient creature. If the triggering damage would cause you to become dying 2 (typically due to a critical hit or your critical failure), you become dying 1 instead. In addition, for 10 minutes, you die from the dying condition at dying 5, rather than dying 4.

> [!danger] Effect: Mortalis Coin

**Source:** `= this.source` (`= this.source-type`)
