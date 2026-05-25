---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 30, 'pp': 0, 'sp': 0}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You keep yourself protected from incoming projectiles with this sturdy steel helmet, painted brown.

**Activate—Block Manipulation** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You gain the [[Stupefied]] condition

**Effect** Your *trusty helmet* protects not only your head but your mind. The value of your stupefied condition is decreased by 1.

**Activate—Hunker Down** `pf2:1` (manipulate)

**Effect** You hunker down, protecting your head using your helmet. You gain a +1 circumstance bonus to your AC against ranged attacks.

**Source:** `= this.source` (`= this.source-type`)
