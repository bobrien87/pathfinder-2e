---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Soothing powders are remedies made to stop a particular type of persistent damage. Each damage type requires a different formula, with the most popular being bleed soothing powder, poison soothing powder, fire soothing powder, and acid soothing powder. You Activate soothing powder by sprinkling it on yourself or another creature within reach. The target can immediately attempt a new flat check to remove persistent damage the powder works against. This powder lowers the DC to 10, as normal for a particularly appropriate type of help.

**Source:** `= this.source` (`= this.source-type`)
