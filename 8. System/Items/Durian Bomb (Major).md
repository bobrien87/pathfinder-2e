---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Olfactory]]", "[[Plant]]", "[[Splash]]"]
price: "{'gp': 2750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Whereas a durian's aroma ranges from pleasant to revolting depending on the person, a durian bomb is a fruit that's been alchemically modified for maximum revulsion. You gain a +3 item bonus to attack rolls.

On a successful Strike, a durian bomb deals the 4d4 piercing damage to the target. Any creature hit by the bomb or in its splash area must attempt a DC 37 [[Fortitude]] save saving throw. Creatures in the splash area treat the results of their saving throw as one step better. Creatures sickened by a durian bomb are unable to smell anything else while the sickened condition lasts, suppressing any scent special sense they might have.

Once a creature is sickened by a durian bomb, they're immune to the sickened condition caused by other durian bombs for 1 minute.
- **Critical Success** The target is unaffected.
- **Success** The creature is [[Sickened]] 1.
- **Failure** The creature is [[Dazzled]] for 1 round and sickened 1.
- **Critical Failure** The creature is dazzled for 1 round and [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
