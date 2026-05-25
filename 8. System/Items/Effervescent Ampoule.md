---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

**Requirements** You're trained in Acrobatics

Light spring water fizzes and bubbles within this small glass globe, spilling onto the affixed armor when activated.

Until the end of your turn, you can move across water and other liquids as if they were solid ground. Your movement does not trigger any device or hazard that relies on a weight-sensitive pressure plate or similar device.

When the ampoule's effect ends, you sink, fall, break through flimsy ground, or land on pressure plates as normal for your current location.

**Source:** `= this.source` (`= this.source-type`)
