---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Comfort]]"]
price: "{'value': {}}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Granted by [[Reinforced Chassis]]

@Embed[Compendium.pf2e.feats-srd.Item.cilZUszwjSGB4p1W inline]

**Source:** `= this.source` (`= this.source-type`)
