---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can use a net either on its own or attached to a rope. When attached to a rope, you can use the net to [[Grapple]] a Medium or smaller creature up to 10 feet away (instead of only adjacent creatures). You can continue to Grapple to keep your hold on the target so long as the target remains within 10 feet and you continue to hold the net. The grabbed creature gains a +2 circumstance bonus to Escape unless you are adjacent to them, and it can attempt a DC 16 [[Athletics]] check to Force Open the net entirely. Once the target is no longer grabbed, the net is unwieldy until refolded with an Interact action with the concentrate trait that requires two hands; if used without being refolded, Grapple checks made with the net take a -2 penalty.

When the net is unattached, you can attempt a ranged attack roll using your simple weapon proficiency against a Medium or smaller creature within 20 feet. On a hit, the target is off-guard and takes a -10- foot circumstance penalty to its Speeds until it Escapes, and on a critical hit, it's also immobilized until it Escapes. The Escape DC is 16 (`act escape dc=16`). A creature adjacent to the target can Interact to remove the net.

**Source:** `= this.source` (`= this.source-type`)
