---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Expandable]]", "[[Magical]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Every *marvelous miniature* is an exceptionally small replica of a real creature or object. The miniature is made from wood, pewter, or other simple materials, and features a rune etched into the underside of the replica's base. *Marvelous miniatures* sometimes come packaged together; for example, the camping set features the boat, campfire, and horse miniatures. Activating a *marvelous miniature* causes it to transform into another creature or object, which then can be used as normal for that object. Each miniature can be activated only once, with most of them permanently becoming the item in their description.

When activated, this miniature transforms permanently into a 20-foot-long wooden ladder.

**Source:** `= this.source` (`= this.source-type`)
