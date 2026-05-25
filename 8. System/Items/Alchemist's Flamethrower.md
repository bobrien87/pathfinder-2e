---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Fire]]"]
price: "{'gp': 35}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long cylinder is topped by a pair of brass sockets and a collection of polished pipes and tubes. A total of two vials of alchemist's fire must be loaded into the sockets at the base of the weapon and the tubes cleaned and primed. Properly loading the flamethrower in this way takes 1 minute. When the trigger on a loaded flamethrower is pulled, the alchemist's fire is siphoned into the rifle and shot out of the muzzle in a line of fire. The damage dealt by a flamethrower is determined by the strength of the weakest alchemist's fire loaded into the flamethrower.

**Activate** `pf2:2` (fire, manipulate)

**Requirements** The flamethrower is loaded

**Effect** You pull the trigger, expending both loaded alchemist's fires to shoot a line of fire. Creatures in the area take fire damage based on the weakest alchemist's fire loaded into the flamethrower, as noted below. Creatures that critically fail the basic Reflex save additionally take the listed persistent fire damage.

- **Lesser Alchemist's Fire**: The flamethrower deals @Damage[1d8[fire]|options:area-damage] (DC 15 [[Reflex]] save) in a @Template[line|distance:30]. 1 persistent,fire damage.
- **Moderate Alchemist's Fire**: The flamethrower deals @Damage[2d8[fire]|options:area-damage] (DC 17 [[Reflex]] save) in a @Template[line|distance:60]. 2 persistent,fire damage.
- **Greater Alchemist's Fire**: The flamethrower deals @Damage[6d8[fire]|options:area-damage] (DC 28 [[Reflex]] save) in a @Template[line|distance:90]. 3 persistent,fire damage.
- **Major Alchemist's Fire**: The flamethrower deals @Damage[10d8[fire]|options:area-damage] (DC 37 [[Reflex]] save) in a @Template[line|distance:120]. 4 persistent,fire damage.

**Source:** `= this.source` (`= this.source-type`)
