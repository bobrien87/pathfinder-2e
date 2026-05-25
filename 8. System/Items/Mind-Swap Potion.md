---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Possession]]", "[[Potion]]"]
price: "{'gp': 1000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Small bolts of brightly colored electricity flicker through the cloudy mind-swap potion. The potion often comes in a double-chambered flask, because when you drink it, you consume half the contents. If another creature of the same ancestry consumes the remainder of the contents within 1 minute, your minds swap per the effect of a critical success on a [[Mind Swap]] ritual. The effects last for 24 hours or until one of you Dismisses the activation.

**Source:** `= this.source` (`= this.source-type`)
