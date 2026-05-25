---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can pull a dueling cape you're wearing from your shoulder and wrap it around your arm with an Interact action. While wielding the dueling cape this way, the cape uses that arm and hand, and you can't hold anything else in that hand.

While you do so, you can spend an action to hold it in a protective position, giving you a +1 circumstance bonus to AC and to Deception checks to [[Feint]] until the start of your next turn.

> [!danger] Effect: Dueling Cape

**Source:** `= this.source` (`= this.source-type`)
