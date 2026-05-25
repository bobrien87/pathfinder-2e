---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1250}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A grinning skull tops the bow of this macabre key. This key can be used in place of thieves' toolkit when attempting to Pick a Lock, and it grants a +2 item bonus to the Thievery check.

If the *skeleton key* becomes broken due to a critical failure on the check, it works as normal thieves' toolkit and loses its benefits until repaired.

**Activate—Loosen Lock** `pf2:f` (manipulate)

**Frequency** once per hour

**Trigger** You attempt to Pick a Lock but haven't rolled yet

**Effect** The key casts [[Knock]] on the lock you're trying to pick.

**Source:** `= this.source` (`= this.source-type`)
