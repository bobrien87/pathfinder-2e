---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 370}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This scepter is made from dragon bone, with minute runes carved along its length, a dragonskin leather grip, and caps of gold on each end. The scepter grants you a +1 item bonus to Intimidation checks to [[Demoralize]]. Such items are considered particularly gruesome and vile by dragons, and they're invariably hostile to any creature they discover carrying a draconic verge, going so far as to single out that individual for destruction.

**Activate—Dragon's Eminence** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You hold the verge aloft, tapping into the majesty of the dragon from whom the verge was made. All enemies in a @Template[type:emanation|distance:60] must succeed a DC 23 [[Will]] save or become [[Frightened]] 2 ([[Frightened]] 3 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
