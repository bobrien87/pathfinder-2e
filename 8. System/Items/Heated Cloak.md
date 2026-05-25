---
type: item
source-type: "Remaster"
level: "5"
price: "{'gp': 160}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fine cloak is lined with tiny tubes of slowly reacting alchemical reagents. These chemicals generate heat, which is circulated throughout the cloak by the wearer's movements. While active, the wearer is protected from severe cold. The cloak offers no protection from extreme or incredible cold. It operates for 24 hours and can be reset with a simple process that takes 1 minute.

**Source:** `= this.source` (`= this.source-type`)
