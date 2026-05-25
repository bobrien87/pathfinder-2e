---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]", "[[Processed]]"]
price: "{'gp': 28}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

This slender bar of pine-scented soap can only be activated when you're immersed in water. Upon activation, the soap covers you in a sudsy foam that quickly fades, filling you with energy and soothing away aches and pains. It immediately restores 10 healing Hit Points and removes the [[Fatigued]] condition. If you begin an 8-hour period of rest immediately after using invigorating soap, you regain an additional 10 Hit Points from resting.

**Source:** `= this.source` (`= this.source-type`)
