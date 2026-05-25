---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Thrown 20]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 trident*, usually engraved with a decorative pattern resembling fish scales, is a common weapon among warriors of aquatic ancestries.

**Activate—Fluid Length** A manipulate

**Effect** You extend or shorten the trident's haft. When extended, the trident requires two hands to wield and gains the reach trait, but loses the trident's normal thrown trait.

**Source:** `= this.source` (`= this.source-type`)
