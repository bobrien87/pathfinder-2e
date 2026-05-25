---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Adjustment]]"]
price: "{'gp': 4}"
usage: "applied-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This armor is easily doffed. A set of armor with armor latches gains the noisy trait; you can't add latches to armor that already possesses the noisy trait. You can remove a set of armor with armor latches with a 3-action activity, which has the manipulate trait. This doesn't affect the time it takes to don the armor.

**Source:** `= this.source` (`= this.source-type`)
