---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Cursed]]", "[[Extradimensional]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item appears to be and functions as a *[[Spacious Pouch (Type I)]]*, until you try to retrieve an item from the bag. Whenever you retrieve an item from the *bag of weasels*, roll a DC 11 flat check. On a success, you retrieve the item as normal. On a failure, the item you retrieve is transformed into a weasel; this doesn't affect artifacts, cursed items, or other hard-to-destroy items.

This weasel uses either the weasel statistics or a giant rat statistics and exudes an aura of magic. The weasel has no loyalty to you and typically attempts to escape as quickly as possible. If the weasel is counteracted, it transforms back into the original item that was taken from the *bag of weasels*. If it dies or is slain, the weasel disappears and the item is permanently destroyed. Because the weasel is a transformed item, you don't gain any benefit you would receive from attacking a creature, defeating one, damaging one, or the like, but you do gain any benefit you would gain from destroying an item.

**Source:** `= this.source` (`= this.source-type`)
