---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 75}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** sling bullet

**Activate** `pf2:1` (manipulate)

This deep-blue glass ball is filled with liquid, and its flight is accompanied by the sound of flowing water. An activated extinguishing ball does no damage. Instead, it bathes the target in a splash of magical water with the following effects, depending on the result of your attack roll.
- **Critical Success** As success, but the water removes all instances of persistent acid or fire damage affecting the target. In addition, it reduces the DC of any future flat checks to end persistent acid or fire damage to 10 for 1 minute, as a particularly appropriate type of assistance to end persistent damage.
- **Success** The water removes one instance of persistent acid or fire damage affecting the target, as if the target had been submerged in water. If the target is taking persistent damage from multiple sources, you select which one is removed. The water aids in ending any remaining sources of persistent acid or fire damage, reducing the DC of the target's next flat check to 10, as a particularly appropriate type of assistance to end persistent damage.
- **Failure** The extinguishing ball misses the target but impacts nearby, splashing the target with enough water to reduce the DC of their next flat check to end one instance of persistent acid or fire damage to 10, as a particularly appropriate type of assistance to end persistent damage.
- **Critical Failure** No effect.

**Source:** `= this.source` (`= this.source-type`)
