---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 15}"
usage: "worn"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of a secret society

This ring has a thick band supporting a square-cut gem that can be customized to the buyer's preference. The thickness of the band allows it to be taken to any jeweler or blacksmith to be adjusted to different hands or fingers from the original make. There is a tiny clasp at the side of the gem that, when pressed, opens the gem, revealing a small, hinged compartment. This compartment is designed to hold one dose of poison, allowing wearers to slip the contents of the ring into the food or drink of an intended target. The compartment can be closed again by gently pressing the gem back into place. Noticing the compartment requires a DC 15 [[Perception]] check for anyone inspecting the ring.

**Source:** `= this.source` (`= this.source-type`)
