---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Acid]]", "[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Disease]]", "[[Splash]]"]
price: "{'gp': 3750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

This flask contains a caustic irritant that makes a target's skin, scales, or carapace extremely sensitive to further nicks and burns. An inflammation flask deals 4d6 acid damage and 4 acid splash damage. On a hit, the target also gains weakness 4 to acid, fire, and slashing damage for 3 rounds. You gain a +3 item bonus to attack rolls.

The target can end the weakness effect by three means: being drenched with water (such as submersion or exposure to an area water effect), being Administered First Aid (DC 38), or regaining Hit Points from a single effect equal to twice the inflammation flask's level. A creature that critically fails to Administer First Aid in this way deals untyped damage to the target equal to the inflammation flask's initial acid damage.

> [!danger] Effect: Inflammation Flask

**Source:** `= this.source` (`= this.source-type`)
