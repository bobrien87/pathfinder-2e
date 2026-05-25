---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bedroll is made of especially fine cotton, stuffed with goose down, and the hem is inscribed with the sigils of the Dreamlands. If you fall asleep in the bedroll, you gain 5 temporary Hit Points that last while you sleep and for 1 minute after you wake up, as well as a +1 status bonus to saves against mental effects that occur while you are asleep, such as the [[Nightmare]] spell.

> [!danger] Effect: Bedroll of Deep Slumber

**Source:** `= this.source` (`= this.source-type`)
