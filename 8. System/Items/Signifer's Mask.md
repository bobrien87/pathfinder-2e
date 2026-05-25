---
type: item
source-type: "Remaster"
level: "0"
price: "{'value': {}}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This mask is often devoid of eyeholes or other decorative features. The mask doesn't obscure your vision, though it makes it impossible for others to see your eyes. While wearing your signifer's mask, you gain a +1 circumstance bonus to Deception checks to `act lie`, Intimidation checks to `act coerce`, and Deception DCs against `act sense-motive`.

**Source:** `= this.source` (`= this.source-type`)
