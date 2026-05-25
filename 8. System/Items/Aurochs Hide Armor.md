---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
bulk: "2"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made of the sturdy, thick hide of the aurochs and tempered to be both flexible and durable, this *+1 resilient hide armor* is imbued with the aurochs' natural defenses against venomous predators. You gain resistance 5 to poison damage.

**Activate—Stubborn Skin** `pf2:1`

You pull the layers of the armor taut, stiffening your body against incoming forces for 1 minute. While the armor is taut, you have a –1 penalty to Reflex saves and a +2 item bonus to Fortitude saves.

> [!danger] Effect: Stubborn Skin

**Source:** `= this.source` (`= this.source-type`)
