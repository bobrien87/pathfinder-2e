---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 420}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These symbols convey protective forces from the Elemental Planes. You gain resistance 5 to acid, cold, electricity, or fire. The crafter chooses the damage type when creating the rune. Multiple *energy-resistant* runes can be etched onto a suit of armor; rather than using only the strongest effect, each must provide resistance to a different damage type. For instance, a *+2 acid-resistant greater fire-resistant breastplate* would give you acid resistance 5 and fire resistance 10.

**Source:** `= this.source` (`= this.source-type`)
