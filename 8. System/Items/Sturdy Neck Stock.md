---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 1300, 'pp': 0, 'sp': 0}"
usage: "worncollar"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thick piece of leather decorated with purple threads makes an attractive necktie but also serves a functional purpose: protecting the neck from hits that you don't see coming. You gain a +1 circumstance bonus to AC against attacks while [[Off Guard]] from flanking.

**Activate—Stretch out Stock** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The sturdy neck stock expands to cover not only your neck but also your shoulders and the back of your head. For 1 minute, you aren't off-guard to [[Hidden]], undetected, or flanking creatures, or creatures using surprise attack of your level or lower.

**Source:** `= this.source` (`= this.source-type`)
