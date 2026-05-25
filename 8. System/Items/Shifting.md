---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 225}"
usage: "etched-onto-melee-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

With a moment of manipulation, you can shift this weapon into a different weapon with a similar form.

**Activate—Shift Weapon** A (manipulate)

**Effect** The weapon takes the shape of another melee weapon that requires the same number of hands to wield. The weapon's runes and any precious material it's made of apply to the weapon's new shape. Any property runes that can't apply to the new form are suppressed until the item takes a shape to which they can apply.

The weapons a *shifting* weapon can turn into are based on the base attributes of the weapon, so reference the weapon's Hands entry in the weapons table to see what it can turn into. For example, a bastard sword requires one hand, even though it gets a benefit in two hands from the two-hand trait. Therefore, a *shifting bastard sword* could turn into a longsword, but not a greatsword. Activating this rune doesn't change how many hands you're currently using to hold the weapon.

**Source:** `= this.source` (`= this.source-type`)
