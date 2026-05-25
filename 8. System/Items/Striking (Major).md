---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Magical]]"]
price: "{'gp': 31065}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *striking* rune stores destructive magic in the weapon, increasing the weapon damage dice it deals to two instead of one. For instance, a *+1 striking dagger* would deal 2d4 damage instead of 1d4 damage.

You can upgrade the *striking* rune already etched on a weapon to a stronger version, increasing the values of the existing rune to those of the new rune. You must have the formula of the stronger rune to do so, and the Price of the upgrade is the difference between the two runes' Prices.

The weapon deals four weapon damage dice.

**Source:** `= this.source` (`= this.source-type`)
