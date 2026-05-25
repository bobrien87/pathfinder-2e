---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Gadget]]", "[[Magical]]"]
price: "{'gp': 70}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you Activate a *nap gas dispenser*, you can either place it in an adjacent space or toss it up to 30 feet away. Once you've done so, the metallic canister instantly disperses knockout gas in a @Template[type:burst|distance:15]. Creatures in the area must attempt a DC 23 [[Fortitude]] save, with the following results. This is a poison and incapacitation effect.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –2 status penalty to Perception checks and is [[Slowed]] 1 for 1 round.
- **Failure** The creature is slowed 1 for 1 minute. At the end of their next turn, they fall [[Prone]] and fall [[Unconscious]] for 1 minute. A creature can Interact to shake the creature awake as normal, but this doesn't shorten the duration of the slowed condition.
- **Critical Failure** As failure, but the creature is slowed 1 for 1 hour and it takes three Interact actions to wake them.

**Source:** `= this.source` (`= this.source-type`)
