---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]"]
price: "{'gp': 19000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sturdy, rigid alchemical chart contains shorthand references on quickly mixing reagents for maximum effect. If you hold this chart while using [[Quick Alchemy]], the items you create of 18th level or lower remain potent for 1 additional round.

**Source:** `= this.source` (`= this.source-type`)
