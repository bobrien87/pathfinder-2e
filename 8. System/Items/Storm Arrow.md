---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Air]]", "[[Consumable]]", "[[Electricity]]", "[[Magical]]"]
price: "{'gp': 130}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

The head of this arrow is made from gleaming copper.

When an activated *storm arrow* hits a target, it is buffeted by raging winds and struck by a bolt of lightning that deals 3d12 electricity damage and the target must attempt a DC 25 [[Reflex]] save saving throw. If this arrow is shot from a weapon with a *shock* property rune, the save DC increases to 27, though the attack doesn't benefit from the *shock* property rune itself.
- **Critical Success** The foe is unaffected.
- **Success** The foe takes half damage and isn't affected by the wind.
- **Failure** The foe takes full damage and is buffeted by winds for 1 round, taking a -2 circumstance penalty to ranged attack rolls and a –10-foot circumstance penalty to its fly Speed.
- **Critical Failure** As failure, but the foe takes double damage.

**Source:** `= this.source` (`= this.source-type`)
