---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Water]]"]
price: "{'gp': 225}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small bag is filled with a fine, silvery powder that feels silky to the touch.

**Activate—Disperse** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You scatter the dust into the air around you, causing it to condense into a cloud in a @Template[burst|distance:20] within 10 feet, as the [[Mist]] spell. You can Sustain the activation to make the cloud Fly 20 feet. The cloud lasts 1 minute, and you can Dismiss it.

**Source:** `= this.source` (`= this.source-type`)
