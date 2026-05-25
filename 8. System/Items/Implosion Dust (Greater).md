---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 4100}"
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

Sealed in a packet so it can be released in a pressurized puff, implosion dust causes amorphous creatures to compress and shrink by hardening and even evaporating the liquid components of their physical forms. It's effective at weakening water elementals, air elementals, oozes, and other creatures the GM determines are similarly amorphous, which can even include particularly gelatinous aberrations. You release the dust toward one creature within 5 feet of you, which must attempt a DC 38 [[Fortitude]] save saving throw. The target must repeat the saving throw at the end of each of its turns. Implosion dust functions for up to 6 rounds. It then becomes inert, and the creature returns to its normal size.
- **Critical Success** The dust becomes inert, and the creature returns to its normal size.
- **Success** The target increases in size one step, up to its normal size. If it's at its normal size after the increase, the effect ends.
- **Failure** The target decreases in size one step, to a minimum of Tiny. The reach of each of its Strikes decreases by 5 feet, to a minimum of 5 feet if the creature is Small or larger, or a minimum of 0 feet if the creature is Tiny. Shrinking also imposes a status penalty to the creature's physical melee damage. This penalty is –2 for every step lower than its normal size the creature is.
- **Critical Failure** As failure, but the target decreases in size by two steps.

**Source:** `= this.source` (`= this.source-type`)
