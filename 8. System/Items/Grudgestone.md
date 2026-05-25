---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 70}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** A creature critically hits you.

This dull black pebble, ominously cold to the touch and curiously heavy for its size, is typically bound to the affixed weapon inside a strip of cloth wrapped around its grip. When you Activate the *grudgestone*, your Strikes with the affixed weapon against the triggering creature gain a +3 status bonus to damage rolls for 1 minute or until the target dies, whichever comes first.

> [!danger] Effect: Grudgestone

**Source:** `= this.source` (`= this.source-type`)
