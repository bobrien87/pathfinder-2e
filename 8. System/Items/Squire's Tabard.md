---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 25, 'pp': 0, 'sp': 0}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Squires with aspirations of being knights wear these loose, colorful tunics, typically emblazoned with the crest of the knight or kingdom they serve.

**Activate—At Your Aid** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You race to the side of an ally who needs your help. You Stride twice, ignoring difficult terrain, but your movement must end adjacent to an ally.

**Source:** `= this.source` (`= this.source-type`)
