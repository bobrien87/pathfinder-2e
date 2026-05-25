---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 450}"
usage: "applied-to-a-basket-bag-or-other-container"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Preserving runes* are common among merchants and other travelers who are on the road for weeks or months at a time. Any non-magical food and drink inside a container with a *greater preserving rune* never spoils. This feature doesn't prolong the duration of alchemical items.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The container casts [[Cleanse Cuisine]] on all the food and drink within.

**Source:** `= this.source` (`= this.source-type`)
