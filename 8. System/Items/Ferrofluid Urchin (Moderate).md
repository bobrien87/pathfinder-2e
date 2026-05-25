---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Metal]]", "[[Talisman]]"]
price: "{'gp': 225}"
usage: "affixed-to-medium-heavy-metal-armor"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Prerequisites** You have the armor specialization effect of the affixed armor

**Trigger** You take physical damage.

This spiky glob of magnetic liquid attaches directly onto the metal of your armor. When you activate the globule, it reshapes to deflect the incoming harm. You gain resistance 6 to the triggering damage.

**Source:** `= this.source` (`= this.source-type`)
