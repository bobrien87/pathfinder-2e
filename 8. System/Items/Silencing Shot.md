---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 300}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

This shimmering, golden-hued ammunition never makes any sound. A creature hit by a *silencing shot* is subject to the effects of a 4th-rank [[Silence]] spell unless it succeeds at a DC 25 [[Will]] save.

**Craft Requirements** Supply one casting of *silence* at 4th rank.

**Source:** `= this.source` (`= this.source-type`)
