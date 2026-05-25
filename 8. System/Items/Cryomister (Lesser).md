---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Cold]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you Activate a cryomister, you can either place it in an adjacent square or toss it up to 20 feet away. Once you've done so, the metallic device instantly disperses a heavy mist, settling quickly on nearby flat surfaces and forming a sheet of ice. The cryomister creates a @Template[type:burst|distance:5], making the affected area difficult terrain for 1 minute; at the GM's discretion, however, this duration might be reduced in unusually hot conditions or increased in unusually cold ones. If an affected square takes fire damage, the difficult terrain is removed. Though not designed as a weapon, the cryomister's rapidly cooling mist deals @Damage[(1[splash])[cold]] splash damage to creatures in the area on activation. Creatures attempting to move through the affected area can attempt a DC 17 [[Acrobatics]] check to ignore the difficult terrain and move at their normal Speed. Throwing the cryomister onto the surface of a liquid creates a floating piece of ice for the same duration, capable of supporting one or more medium creatures.

**Source:** `= this.source` (`= this.source-type`)
