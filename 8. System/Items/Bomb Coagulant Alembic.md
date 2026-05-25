---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]"]
price: "{'gp': 150}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This apparatus increases the viscosity of the reagents in alchemical bombs, to deadly effect. As a 10-minute activity that has the manipulate trait, you can use a bomb coagulant alembic to distill the contents of one infused alchemical bomb that deals splash damage into a stickier substance. After distilling, the bomb deals no splash damage but instead deals persistent damage equal to and of the same type as its original splash damage. If the bomb already deals persistent damage, distilling increases that damage by the bomb's original splash damage.

**Source:** `= this.source` (`= this.source-type`)
