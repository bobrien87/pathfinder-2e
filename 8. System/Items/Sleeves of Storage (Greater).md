---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Extradimensional]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 600}"
usage: "worngarment"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This loose robe has wide, voluminous sleeves that each contain an extradimensional space. These spaces each function as a [[Spacious Pouch (Type I)]] that can hold up to 20 Bulk of items (for a total of 40 Bulk), though no individual item can be of more than 1 Bulk; the sleeves grow slightly heavy as you reach maximum capacity. You can add or remove an item from a sleeve with a single hand free as an Interact action.

If a sleeve is completely empty, you can place your own familiar into that extradimensional space. It can survive comfortably in your sleeve for up to 4 hours, after which it begins to *suffocate*. While in your sleeve, it can't be affected or targeted by any effects, but you don't benefit from any master abilities. A familiar can exit the sleeve of its own volition with a single action that has the *manipulate* and *move* traits. You can't place any other creature into your sleeves, nor can you place your familiar in a sleeve if it's larger than Tiny. If your familiar is in your sleeve, you can't place any items in the sleeve.

**Source:** `= this.source` (`= this.source-type`)
