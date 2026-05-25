---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Earth]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Life-infused soil from the Plane of Earth, *vital earth* is glittering dust you inhale that causes you to not need air or water for 24 hours. Also, for this time, your wounds close easily, like molding clay, meaning someone attempting to [[Administer First Aid]] or [[Treat Wounds]] on you doesn't need a healer's toolkit and gains a +1 item bonus to the Medicine check.

**Source:** `= this.source` (`= this.source-type`)
