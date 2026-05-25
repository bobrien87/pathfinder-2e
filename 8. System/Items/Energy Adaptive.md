---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 2600}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A complex pattern of protective symbols gives protection against various forms of energy, but only part of the runic structure can be active at a given time.

**Activate**R (concentrate)

**Frequency** once per hour

**Trigger** You take acid, cold, electricity, or fire damage

**Effect** You gain resistance 5 to the triggering damage type. This doesn't apply to the triggering damage. This resistance lasts until you Activate this rune again or the armor is no longer invested by you.

> [!danger] Effect: Energy Adaptive

**Source:** `= this.source` (`= this.source-type`)
