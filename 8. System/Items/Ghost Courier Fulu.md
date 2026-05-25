---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

The inscription on a *ghost courier fulu* leaves space for a message, and a prominent red stamp indicates which ghost delivery fulu this fulu homes in on (see below). When you Activate this fulu, you dictate a message up to 25 words long that then magically appears on the paper in the language you spoke. The fulu then disappears into the Ethereal Plane, arriving at the assigned ghost delivery fulu in 2d10 hours, provided that fulu is within 500 miles. There, the fulu's magic dissipates, but the message remains. If the fulu takes any damage in transit, it has a 50% chance to drop back into the Universe, intact but bereft of magic.

**Source:** `= this.source` (`= this.source-type`)
