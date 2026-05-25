---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Acid]]", "[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Plant]]", "[[Splash]]"]
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

**Activate** `pf2:1` Strike

Made from the acidic flesh of an especially astringent fruit found on the Plane of Wood, this bomb's contents soften, oxidize, and season whatever they touch. You gain a +3 item bonus to attack rolls.

On a successful Strike, a tenderizer grenade deals the 4d6 acid damage to the target and the 4 acid splash damage. Any resistances the target has against bludgeoning, piercing, and slashing damage are reduced by an amount based on the bomb's type. In addition, the target is showered with appetizing esters, oils, and salts, making them [[Off Guard]] against jaws Strikes, fangs Strikes, or similar Strikes with a creature's mouth. These additional effects last until the end of your next turn, or for 1 minute on a critical hit.

**Source:** `= this.source` (`= this.source-type`)
