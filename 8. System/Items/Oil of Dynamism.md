---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 85}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This fine golden oil comes in a small blue canister. Carefully spreading the oil over an object turns it into an *animated object* of the same type. For example, sprinkling it on a statue makes an *animated statue*. If the animated object's level would be greater than 3, the oil struggles to animate it and ultimately fails.

This animated object has the *minion* trait, meaning it can use 2 actions when you Command it. You can issue a Command for the current turn as part of the activation. The object remains animated for 1 minute before falling inert. As usual, you can have a maximum of four minions under your control.

**Source:** `= this.source` (`= this.source-type`)
