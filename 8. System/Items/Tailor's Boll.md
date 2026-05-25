---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

Harvested from one of the rainbow fields of the Plane of Wood, this cotton boll is filled with multicolored fibers. When you Activate the boll, you make a request for a bespoke set of non-magical explorer's clothing or fine clothing. The hard fibers and seeds leap from your hand to spin and weave, cotton flying through the air at incredible speed to make cloth and thread. The clothing is ready at the start of your next turn, in the most convenient spot nearby for hanging the clothing or laying it flat.

If you hold clothing in your other hand when you activate the boll, the boll instead reweaves that item to match the style you specified. This can't change the type of item; you couldn't turn fine clothing into explorer's clothing or winter clothing, for example.

**Source:** `= this.source` (`= this.source-type`)
