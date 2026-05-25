---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1300}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item consists of two magically linked rings: an intricate, gleaming golden ring with a square-cut ruby, and a thick, plain iron ring. When you wield a melee weapon in the hand wearing the golden ring, the weapon's fundamental runes are replicated onto any melee weapon you wield in the hand wearing the iron ring. (The fundamental runes are *weapon potency* and *striking*, which add an item bonus to attack rolls and extra weapon damage dice, respectively.) Any fundamental runes on the weapon in the hand wearing the iron ring are suppressed.

The replication functions only if you wear both rings, and it ends as soon as you cease wielding a melee weapon in one of your hands. Consequently, the benefit doesn't apply to thrown attacks or if you're holding a weapon but not wielding it (such as holding in one hand a weapon that requires two hands to wield).

The rings also replicate property runes from the weapon in the gold-ringed hand, so long as the weapon in the iron-ringed hand meets all the prerequisites for a given rune and is not a specific weapon. The weapon in the iron-ringed hand gains the benefits of those runes. All its own runes are suppressed. When you invest the rings, you can elect for the rings to transfer only fundamental runes, in which case they function as standard *doubling rings*.

**Source:** `= this.source` (`= this.source-type`)
