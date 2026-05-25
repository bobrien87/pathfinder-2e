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

Alchemical reagents add punch to tracker's stew: a rich, fiery mixture of tomatoes, ground nuts, onions, and tubers, often with poultry added. It's usually served with or over rice or noodles. Once you've eaten the stew, it improves your ability to sense and follow tracks for 24 hours or until you make your next daily preparations, whichever comes first. You gain a +1 item bonus to Survival checks to Cover Tracks and [[Track]]. You can do either while moving at full speed or both while moving at half speed.

> [!danger] Effect: Tracker's Stew

**Source:** `= this.source` (`= this.source-type`)
