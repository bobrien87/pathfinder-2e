---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Poison]]", "[[Splash]]"]
price: "{'gp': 4000}"
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

The Verduran Forest's tiny tent-trap spider lays her eggs in a pyramidal web, and her young hatch only in response to intense vibration, such as the struggles of an ensnared insect or even songbird. Sadistic alchemists gather and augment these eggs, packing them in silken satchels that disgorge thousands of biting spider babies on impact.

Until shaken off—or for the desperate target, incinerated—these spiders make it difficult to concentrate on anything other than escaping the swarm. The fascination effect ends automatically if a creature uses further hostile actions against the target, but hostile actions against the target's allies don't automatically end the effect.

You gain a +3 item bonus to attack rolls. The bomb deals 4d6 persistent poison damage, 4 poison splash damage, and fascinates the target while the persistent damage lasts.

**Source:** `= this.source` (`= this.source-type`)
