---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Splash]]", "[[Vitality]]"]
price: "{'gp': 2500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

These spring-loaded metal canisters contain a mixture of chemicals and salts that drain and disintegrate nearby undead creatures.

A *ghost charge* gives a +3 item bonus to attack rolls, deals 4d8 vitality damage and 4 vitality splash damage, though as usual for vitality damage, this damage harms only undead and creatures with void healing. A primary target that takes damage from a *ghost charge* becomes [[Enfeebled]] 2 until the start of your next turn.

*Ghost charges* are designed to explode even on contact with a spiritual substance, making them ideal for damaging incorporeal undead.

**Source:** `= this.source` (`= this.source-type`)
