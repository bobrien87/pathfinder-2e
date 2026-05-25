---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Air]]", "[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 2000, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

As this magical banner sways in the breeze, the horses embroidered across the fabric seem to gallop at unnatural speeds, racing across the field. You and allies that start your turn within the banner's aura gain a +5-foot status bonus to land Speeds for 1 round. This bonus is doubled while traveling.

> [!danger] Effect: Swift Standard

**Source:** `= this.source` (`= this.source-type`)
