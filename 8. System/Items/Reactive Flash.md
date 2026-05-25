---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 27, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

These whetstones are miniature stone replicas of weapons, such as a sword or an axe, though their function is the same regardless of their shape. When you attempt a Strike as a reaction (such as with a [[Readied]] action or the [[Reactive Strike]] reaction) using a weapon under the effect of a *reactive flash*, the target must first succeed at a DC 19 [[Reflex]] save or be [[Off Guard]] against the attack.

**Source:** `= this.source` (`= this.source-type`)
