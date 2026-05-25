---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 40}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You create a snare that causes three 3rd-level moderate alchemical bombs of the same type to explode when a creature triggers the snare. The target and all creatures in adjacent squares must attempt a [[Reflex]] save, as the snare deals damage equal to three times the direct hit damage from one of the component bombs (for example, 6d6 electricity damage from three moderate bottled lightnings) with no splash damage or other effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and no other effects.
- **Failure** The creature takes full damage. It also takes all other effects of a direct hit from one of the component bombs (such as [[Off Guard]] from bottled lightning or persistent damage from an acid flask).
- **Critical Failure** The creature takes double damage, plus all other effects of a direct hit (as failure).

**Craft Requirements** Supply three of the same damaging 3rd-level moderate alchemical bomb.

**Source:** `= this.source` (`= this.source-type`)
