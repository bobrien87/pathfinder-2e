---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 2400}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** Your Strike damages a target

Made from a treated sliver of cold iron, this talisman allows you to counteract magical effects. When you activate the *dispelling sliver*, it attempts to counteract a single spell active on the target (counteract modifier +29), with the effects of an 8th-rank [[Dispel Magic]] spell. If you activate the talisman on a successful [[Dispelling Slice]], the talisman attempts to counteract all spells active on the target, in addition to your attempt from Dispelling Slice.

**Source:** `= this.source` (`= this.source-type`)
