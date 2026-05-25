---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Olfactory]]"]
price: "{'gp': 3000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This alchemical candle is attached to a tall pole and grounding stake. When the flare is lit, it sprays a concentrated cloud of pheromones to attract the attention of a specific kind of animal (see alchemical pheromones). Similar to animal pheromones, when you learn the formula for a pheromone flare, you learn the formulas for all common animals.

A pheromone flare has a built-in delayed activation timer of up to 1 hour. When it's activated, the flare releases a cloud of pheromones in a @Template[emanation|distance:60] that lasts for 1 hour. A strong wind reduces the emanation to @Template[emanation|distance:15]{15 feet} for as long as the wind lasts. Moving the flare after it has been activated ends the effect. A designated animal that enters the area must attempt a DC 35 [[Will]] save with the following effects. Animals with an Intelligence modifier of –3 or higher increase the result of their save by one step.
- **Critical Success** The animal is unaffected and temporarily immune for 24 hours.
- **Success** The animal is unaffected but must attempt a new save every 10 minutes it remains within the area.
- **Failure** The animal is attracted by the pheromones, following the cloud to its source. The creature becomes [[Fascinated]] until it reaches the flare and spends 1 round investigating it. After this, it becomes temporarily immune for 24 hours.
- **Critical Failure** As failure, except the fascination lasts for up to 1 hour, though the animal can attempt a new save against the effect every 10 minutes. The animal takes a –1 status penalty to this save that increases by 1 with each subsequent failure or critical failure, up to a maximum of a –3 status penalty

**Source:** `= this.source` (`= this.source-type`)
