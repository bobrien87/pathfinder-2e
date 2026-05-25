---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This very small shield is a favorite of duelists and quick, lightly armored warriors. It's typically made of steel and strapped to your forearm. You can [[Raise a Shield]] with your buckler as long as you have that hand free or are holding a light object that's not a weapon in that hand.

HardnessHPBT363

**Source:** `= this.source` (`= this.source-type`)
