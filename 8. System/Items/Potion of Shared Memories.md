---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Potion]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A potion of *shared memories* can transfer recollections from one creature to another. To place a memory in the potion, you must hold the vial and focus on a particular memory for 1 minute. This memory must be of a single event, location, person, or otherwise encompass a span of about 1 minute. The clear fluid takes on a shimmering hue reminiscent of the stored memory and gains a slightly sweet taste.

Upon consuming the potion, the drinker vividly recalls the memory, and thereafter can remember it as easily as a memory they actually experienced. An unwilling drinker can refuse to absorb the memory.

**Source:** `= this.source` (`= this.source-type`)
