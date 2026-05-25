---
type: item
source-type: "Remaster"
level: "17"
price: "{'gp': 5000}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can manacle someone who is willing or otherwise at your mercy as an exploration activity taking 10-30 seconds depending on the creature's size and how many manacles you apply. A two-legged creature with its legs bound takes a –15-foot circumstance penalty to its Speeds, and a two-handed creature with its wrists bound has to succeed at a DC 5 flat check any time it uses a manipulate action or else that action fails. This DC may be higher depending on how tightly the manacles constrain the hands. A creature bound to a stationary object is immobilized. For creatures with more or fewer limbs, the GM determines what effect manacles have, if any. Freeing a creature from superior manacles requires six successful DC 42 [[Thievery]] check.

**Source:** `= this.source` (`= this.source-type`)
