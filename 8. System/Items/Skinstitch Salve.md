---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sticky salve stubbornly holds wounds closed and encourages swift natural healing. You can activate the salve in either of the following ways.

**Activate—Administer Stitch** `pf2:1` (manipulate)

**Effect** You [[Administer First Aid]] without requiring [[Healer's Toolkit]]. You either gain a +2 item bonus to the Medicine check, or you can use the skinstitch salve's Medicine modifier of `r 1d20+13` instead of your own.

**Activate—Stitch Wounds** `pf2:f` (manipulate)

**Trigger** You [[Treat Wounds]] or use [[Battle Medicine]]

**Effect** You gain a +2 item bonus to the triggering Medicine check. If you roll a success on the Medicine check, you get a critical success instead.

> [!danger] Effect: Skinstitch Salve

**Source:** `= this.source` (`= this.source-type`)
