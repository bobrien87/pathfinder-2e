---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

The baubles wemmuths use to lure victims to their hunting grounds are dangerous to retrieve and often stained by blood. One of these trinkets covers the plant matter created by [[Entangling Flora]] with blood-drinking thorns. Creatures who fail or critically fail their Reflex saves against *entangling flora* also take piercing damage equal to the spell's rank.

> [!danger] Effect: Wemmuth Trinket

**Source:** `= this.source` (`= this.source-type`)
