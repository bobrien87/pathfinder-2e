---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** You're a member of the Lion Blades.

When collapsed, a *fan buckler* appears to be no more than an elegant wooden fan. Any attempts to discern that there's more to the item require a successful Perception check against the Deception DC of the wielder.

**Activate—Unfurl Fan** `pf2:1` (manipulate)

**Effect** You transform the fan into a wooden [[Buckler]] (Hardness 3, HP 6, BT 3) or vice versa.

**Source:** `= this.source` (`= this.source-type`)
