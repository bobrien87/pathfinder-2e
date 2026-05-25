---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 90, 'pp': 0, 'sp': 0}"
usage: "worncloak"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hooded cloak is lined with rough foliage, vines, and bark that never wilts or rots away. When wearing this cloak, you gain a +1 item bonus to Stealth checks when in heavily forested areas.

**Activate—One with the Woods** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** For the next minute, you ignore any difficult terrain caused by plants and fungi, such as bushes, vines, and undergrowth.

**Source:** `= this.source` (`= this.source-type`)
