---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 25}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather sheath is large enough to hold an item of up to light Bulk and is typically used for daggers, wands, thieves' tools, and similar objects.

You can affix it to the inside of a boot, under a bracer or sleeve, or in other inconspicuous locations to gain a +1 item bonus to Stealth checks and DCs to hide or conceal the item within.

**Source:** `= this.source` (`= this.source-type`)
