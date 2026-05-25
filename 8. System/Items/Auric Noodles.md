---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 10}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

Auric noodles are boiled, then pan-fried and tossed with sliced vegetables and a sticky, savory sauce incorporating alchemical reagents. After you eat the noodles, they boost your ability to sense magic for 24 hours or until you make your next daily preparations, whichever comes first. You gain a +1 item bonus to checks to Identify Magic, and you can move at full speed while using the [[Detect Magic]] exploration activity.

> [!danger] Effect: Auric Noodles

**Source:** `= this.source` (`= this.source-type`)
