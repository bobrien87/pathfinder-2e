---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Arcane]]", "[[Invested]]"]
price: "{'gp': 50}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hat comes in many forms, such as a colorful turban or a pointy hat with a brim, and is adorned with symbols or runes. It grants you a +1 item bonus to Arcana checks and allows you to cast the  cantrip as an arcane innate cantrip.

**Source:** `= this.source` (`= this.source-type`)
