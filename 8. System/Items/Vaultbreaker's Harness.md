---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 230}"
usage: "wornbackpack"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *vaultbreaker's harness* has four pockets across the chest. The pockets contain a set of [[Thieves' Toolkit (Infiltrator)]], [[Thieves' Toolkit (Infiltrator Picks)]], a [[Crowbar (Levered)]], and a [[Glass Cutter]]. These items are magically bound to the harness; if they are more than 1 foot away from you, they disappear, then reappear in the harness at the next sunset. Broken or destroyed items similarly reappear, restored, in their proper pockets at sunset.

**Activate** `pf2:1` (manipulate)

**Effect** You cinch the harness to prepare for mischief. You gain a +1 item bonus to Stealth checks and a +10-foot item bonus to your Speed for 1 minute.

> [!danger] Effect: Vaultbreaker's Harness

**Source:** `= this.source` (`= this.source-type`)
