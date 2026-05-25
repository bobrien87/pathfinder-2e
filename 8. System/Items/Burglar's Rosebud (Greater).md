---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Emotion]]", "[[Mental]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Though originally intended to protect a green man's favorite agents against predation by pesky herbivores, thieves have adapted the design to help them disperse guard animals. The soft flower bud belies the horrible perfume contained within. Activated by cracking open the petals, the rosebud exudes a noxious cloud that has the olfactory trait for 10 minutes. If dropped, it fills a 10-foot-burst. If you carry it in one hand and periodically waft it as a free action, the rosebud instead gives you a @Template[emanation|distance:10]. Creatures that enter or start their turn in the cloud must succeed at a DC 24 [[Fortitude]] save or become [[Sickened]] 1. Animals and beasts that critically fail are also [[Fleeing]] for 1 round. A creature that successfully saves against the burglar's rosebud becomes temporarily immune to the effects for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
