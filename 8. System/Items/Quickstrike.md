---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]"]
price: "{'gp': 10000}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Attacks with a *quickstrike* weapon are supernaturally swift. While wielding a *quickstrike* weapon, you gain the quickened condition, but you can use the additional action granted only to make a Strike with the etched weapon.

**Source:** `= this.source` (`= this.source-type`)
