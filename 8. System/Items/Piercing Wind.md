---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Combination]]", "[[Concussive]]", "[[Fatal aim d10]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Favored by caravan guards who traverse the Mana Wastes, a piercing wind is similar to a [[Jezail]], in that you can carry it in one hand as long as the other hand's free, by holding it under one arm. Additionally, it's fitted with an underslung curved blade.

**Source:** `= this.source` (`= this.source-type`)
