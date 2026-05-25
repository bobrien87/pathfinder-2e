---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Sonic]]"]
price: "{'gp': 3600}"
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

Ripples move constantly through a roaring potion, a cloudy liquid that growls when you open its container. Drinking it gives you access to two other activations for 1 hour.

**Activate** `pf2:1` (concentrate)

**Effect** You gain the effects of a 7th-rank [[Bullhorn]] spell. You can Dismiss the activation.

**Activate** `pf2:1` (concentrate)

**Frequency** once every 1d4 rounds

**Effect** You emit a scream in a @Template[cone|distance:15] that deals @Damage[10d4[sonic]|options:area-damage]. Each creature in the area can attempt a DC 38 [[Fortitude]] save saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Frightened]] 1.
- **Critical Failure** The creature takes double damage and is [[Frightened]] 2.

**Source:** `= this.source` (`= this.source-type`)
