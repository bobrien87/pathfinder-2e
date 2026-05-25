---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'cp': 0, 'gp': 40, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This dull red stone is shot through with glittering veins of black and silver. When you apply a *slayer's stone* to your weapon, choose aberration, animal, beast, celestial, construct, dragon, elemental, fey, fiend, giant, monitor, ooze, or both fungus and plant. A weapon under the effect of a *slayer's stone* deals an additional 1d6 precision damage to the creatures with the chosen trait or traits for 1 minute. It's up to the GM's discretion whether this benefit applies against a creature disguised as a creature with the chosen trait or traits.

> [!danger] Effect: Slayer's Stone

**Source:** `= this.source` (`= this.source-type`)
