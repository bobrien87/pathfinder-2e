---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Artifact]]", "[[Divine]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ruby-studded dawnsilver chalice can't be harmed by any substance it holds, no matter how caustic. Furthermore, liquid placed within the *Chalice of Ozem* never spills unless its carrier chooses to do so (using a single action with the concentrate trait).

**Activate—Iomedae's Blessing** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You hold the chalice and call out Iomedae's name. The chalice casts [[Dispelling Globe]] with a +19 modifier to its counteract check.

**Destruction** If the *Chalice of Ozem* is filled with Iomedae's blood and Arazni drinks from it, it shatters.

**Source:** `= this.source` (`= this.source-type`)
