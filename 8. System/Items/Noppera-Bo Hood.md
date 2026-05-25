---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Illusion]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 85}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This unpleasant-looking hood appears to be a completely smooth, round sack of skin that feels uncannily warm to the touch. When you wear this hood and invest it, it merges with your head and face, becoming imperceptible as a worn item except on close examination, which reveals a slight oily sheen to your facial features. You can cause minor shifts and changes to your features while wearing a *noppera-bo hood*; this counts as having a disguise kit to Impersonate any creature that's the same ancestry as you.

**Activate—Another Face** `pf2:2` (concentrate, morph)

**Frequency** once per day

**Effect** You focus on the hood's magic, and then gain the effects of a 1st-rank [[Illusory Disguise]] spell, though it's a morph effect rather than an illusion effect.

**Source:** `= this.source` (`= this.source-type`)
