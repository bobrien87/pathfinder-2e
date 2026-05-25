---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate)

**Requirements** You're [[Grabbed]] or [[Restrained]].

When rogues and scoundrels find themselves in sticky situations, a greased axle is a quick way out. You attempt a check to [[Escape]], with a +1 item bonus to your check. If you critically fail, you get a failure instead.

> [!danger] Effect: Greased Axle

**Source:** `= this.source` (`= this.source-type`)
