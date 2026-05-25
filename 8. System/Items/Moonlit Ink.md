---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Member of a secret society

This alchemical ink is applied to a stamping device, typically a wooden seal or chop commissioned by the secret society and costing 1 sp. When the seal is pressed to paper, the ink briefly shows up before fading into invisibility. The stamp can be revealed by exposing the stamped item to direct moonlight for 1 minute. A character checking a good or document marked by a moonlit ink stamp must succeed at a DC 25 [[Perception]] check to spot the stamp without exposure to moonlight. In addition to its use by secret societies for their secret books, papers, and messages, some smugglers use moonlit ink to mark their goods.

**Source:** `= this.source` (`= this.source-type`)
