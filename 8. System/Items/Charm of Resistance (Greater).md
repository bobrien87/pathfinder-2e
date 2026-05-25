---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 975}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This charm, normally hung from the belt or worn around the neck, grants you resistance 10 against one type of energy damage: acid, cold, electricity, fire, or sonic. Each charm is crafted to protect against a particular type of energy damage, and its design usually embodies the type of energy it protects the wearer from in some way. For instance, a *charm of cold resistance* could be carved in the shape of a yeti, whereas a *charm of fire resistance* would be made from volcanic glass.

**Source:** `= this.source` (`= this.source-type`)
