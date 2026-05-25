---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 200}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Before it's activated, this item appears to be an ash rod capped with steel on either end.

**Activate—Tap** `pf2:2` (concentrate, manipulate)

**Effect** You imagine a specific simple tool, and the any-tool transforms into it. (Usually, you can choose from a tool listed in the gear from Player Core). This transforms the wooden portion into any haft and the metal caps into spades, hammer heads, or the like, allowing for most basic tools but nothing more complex. You can return the item to its rod form with an Interact action.

**Source:** `= this.source` (`= this.source-type`)
