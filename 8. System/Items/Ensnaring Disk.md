---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 70}"
usage: "affixed-to-a-shield"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You use the affixed shield to Shield Block a melee weapon attack

**Requirements** You are an expert in Athletics.

This coin-sized metal disk is inscribed with arcane symbols and mounted on the inner surface of a shield. When you Activate the disk, the triggering weapon momentarily sticks to your shield, allowing you to attempt to [[Disarm]] it from its wielder with a +2 item bonus. If you roll a critical failure on this check, you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
