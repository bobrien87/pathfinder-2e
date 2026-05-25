---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Divine]]"]
price: "{'gp': 19000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This brass censer dangles on a length of chain. Most *thuribles of revelation* are adorned with swirling Empyrean text, though some are iron and feature Diabolic or Chthonian text.

**Activate—Burn Incense** `pf2:2` (manipulate)

**Cost** incense worth at least 5 gp

**Effect** You light the incense inside the censer, and it burns for 1 hour. During that time, as long you are holding the thurible, you gain a +3 item bonus to Religion checks, and any critical failure you roll when you Decipher Writing of a religious nature is a failure instead.

Once per day, when you activate the thurible, you can increase its revelations. During that activation, you can hold the thurible up to your eyes with an Interact action to gain the effects of [[See the Unseen]] and [[Truesight]] for 1 round by peering through the smoke.

> [!danger] Effect: Thurible of Revelation

**Source:** `= this.source` (`= this.source-type`)
