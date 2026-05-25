---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Missive]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

A messenger missive sends itself. When composing the missive, you write a location upon it. You can also include an individual creature you expect to be in that location as a recipient; if you don't, the first creature in the location to touch the missive is treated as the recipient. Once you finish composing the missive, it folds itself into the shape of a bird and Flies at a Speed of 45 feet (15 miles per hour) toward the location for up to 24 hours. It alights near its recipient or in their hand. When activated, the missive becomes non-magical but retains its contents. If it fails to reach its recipient in 24 hours, the missive burns to ash.

You can write up to four locations on the missive, one on each edge of the paper; you can include a recipient for each location, as well. When you finish composing the missive, it folds into four identical missive birds, each one flying to one of the locations carrying the same message.

**Source:** `= this.source` (`= this.source-type`)
