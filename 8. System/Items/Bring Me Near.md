---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Teleportation]]"]
price: "{'gp': 1800}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This collapsible Fine Spyglass consists of 3 leather tubes that slide into one another. The edge of each is trimmed in silver, and the lenses are made of finely crafted glass. While looking through it, you gain a +2 item bonus to any Perception checks made involving sight.

**Activate** 1 minute (concentrate, manipulate)

**Frequency** once per day

**Effect** You focus on any spot you can see within 5 miles through the spyglass and rotate its parts in a meticulous order. You and up to 4 willing creatures adjacent to you are instantly teleported to that spot. If there's not enough room for everyone, only you are transported. If there's not enough room for you, the teleportation fails.

**Source:** `= this.source` (`= this.source-type`)
