---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 190}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` Interact

A malformed, artificial brain pulses with alchemical life inside a nutrient-rich vat. When the vat-grown brain is activated, it attempts to counteract one condition of your choice that was gained from an ability with the mental trait, which it does by drawing the negative mental impressions into itself. However, the artificial brain is not robust, and the strain of the transfer quickly destroys it. The vat-grown brain has a counteract rank of 5 and a +17 modifier on the roll.

**Source:** `= this.source` (`= this.source-type`)
