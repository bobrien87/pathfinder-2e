---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 30, 'pp': 0, 'sp': 0}"
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

Originally created by Taldan cavaliers acting as knights errant, *chivalric emblems* have since spread across the Inner Sea region and beyond. A *chivalric emblem* is crafted in the form of a small iron shield, embossed with heraldic insignia. These whetstones call protective spirits into a weapon; the effects last for 1 hour. While wielding a weapon under the effect of a *chivalric emblem*, if you witness an ally being reduced to 0 Hit Points or taking damage from a critical Strike, you gain a +1 circumstance bonus to attack rolls and damage with that weapon against the creature that damaged that ally for the remainder of the *chivalric emblem*'s duration.

> [!danger] Effect: Chivalric Emblem

**Source:** `= this.source` (`= this.source-type`)
