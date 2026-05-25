---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Slivers of boar tusk are sewn into this leather cap, creating a scaled helmet that channels dozens of boars' ferocity into the wearer.

**Activate—Boar's Last Stand** `pf2:1` (auditory, concentrate)

**Frequency** once per day

**Trigger** Your turn begins

**Requirements** You have a doomed or wounded value of 1 or higher

**Effect** You unleash a fearsome roar. 1 creature of your choice within 30 feet must attempt a DC 16 [[Will]] save or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure). Increase this DC by the sum of your [[Doomed]] and [[Wounded]] values (maximum DC 20). You then gain 5 temporary Hit Points that last 1 minute.

**Source:** `= this.source` (`= this.source-type`)
