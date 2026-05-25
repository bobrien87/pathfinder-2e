---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Shadow]]", "[[Teleportation]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (concentrate, manipulate)

This stick of dark-gray incense carries a faint, strange odor that's different for any creature that smells it—mimicking a scent that evokes feelings of nostalgia or homesickness. You begin the activation of a stick of netherwalk incense by lighting it on fire as a single Interact action, at which point you designate up to 10 willing creatures within 20 feet of you. After spending a minute concentrating on the smoke and its scent, you and the affected creatures move into the Netherworld and can use its warped nature to speed travel. Each hour, your travel covers a distance of 50 miles, during which landmarks appear as vague and symbolic images rather than concrete visuals. You arrive within a mile of your intended destination when you Dismiss the effect or after 8 hours have passed.

**Source:** `= this.source` (`= this.source-type`)
