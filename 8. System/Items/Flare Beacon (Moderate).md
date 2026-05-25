---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 35}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Flare beacons create an incredibly bright light for a brief period of time. They are often used to signal others to the beacon's location, to coordinate assaults, to request rescue, or for other similar reasons. Higher-level beacons have a radius so large that they can be seen from miles away at night. When you Activate a flare beacon, you can either place it on the ground in a space within your reach or toss it up to 60 feet straight up.

The beacon then sparks into being, casting bright light in a 60-foot radius and dim light in the next 60 feet for 1 minute. A flare beacon in the air falls at a rate of 10 feet per round. Creatures within a @Template[emanation|distance:10]{10-foot radius} of the beacon must succeed at a DC 20 [[Fortitude]] save or be [[Dazzled]] until they are no longer within 10 feet of it.

**Source:** `= this.source` (`= this.source-type`)
