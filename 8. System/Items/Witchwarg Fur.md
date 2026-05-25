---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 52}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

The pelt of a witchwarg stays cold long after it leaves the creature's body. A tuft of this fur can freeze a [[Fire Shield]] spell into solid ice, inverting its usual effects. The spell's fire trait is replaced with the cold trait, you gain resistance to fire damage and environmental heat effects (instead of cold effects), the shield is immune to cold damage instead of fire damage, and its Hardness is halved against fire effects. The damage you deal to creatures that touch you or hit you with a melee or unarmed attack has its type changed to cold.

**Source:** `= this.source` (`= this.source-type`)
