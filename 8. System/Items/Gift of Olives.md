---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Plant]]"]
price: "{'gp': 48}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This expertly trimmed olive branch remains lush and vibrant, even months after being ritually harvested. With a little soil and patience, it can quickly grow into a sheltering tree that later bestows the user with a new *gift of olives*.

**Activate—Sew the Cutting** `pf2:2` (healing, manipulate, plant)

**Requirements** You are outside and standing atop an unoccupied 5-foot square with some soil

**Frequency** once per day

**Effect** You drive one end of the cutting into the soil. The cutting immediately grows into an olive tree whose boughs shelter a 15-foot-diameter area. Creatures in the sheltered area gain resistance 3 to any environmental damage, gain a +1 status bonus to saving throws against environmental hazards, and gain a +1 status bonus to Survival checks to Subsist. After 10 minutes, the tree sprouts 8 olives, each of which can be eaten as an action to restore 1 Hit Point and nourish the eater as if they had consumed a full meal. After 8 hours, the olives lose their potency, and the *gift of olives* cutting detaches from the tree and falls harmlessly to the ground. The olive tree loses its protective abilities and becomes a normal, non-magical olive tree that survives so long as it's growing in a suitable location.

**Source:** `= this.source` (`= this.source-type`)
