---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Upon smashing this ball on the ground, you instantly create a screen of thick, opaque smoke in a @Template[burst|distance:5] centered on one corner of your space. All creatures within that area are [[Concealed]], and all other creatures are concealed to them. The smoke lasts for 1 minute or until dispersed by a strong wind.

**Source:** `= this.source` (`= this.source-type`)
