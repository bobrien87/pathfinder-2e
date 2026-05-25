---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Trip]]"]
price: "{'gp': 340}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking scythe* is made from the cruel, blackened branches of the carnivorous scythe tree, which hungrily drink up spilled blood.

**Activate—Root in Blood** `pf2:1` (manipulate)

**Requirements** Your last action was a successful Strike with this weapon and your target isn't currently taking any persistent bleed damage

**Effect** You break off a piece of the *bloodgorger scythe* inside your enemy to feed on their blood and sprout into a new tree. The target takes 1 bleed damage at the end of their turn. Each failure to stop the bleeding increases this bleed damage by 1 as a small scythe tree grows from the wound, to a maximum of 3 persistent bleed damage.

**Activate—Sapling Slash** `pf2:1` (concentrate)

**Requirements** A target has a piece of the *bloodgorger scythe* broken off inside them and has failed to recover from the persistent bleed damage for 3 consecutive turns

**Effect** The sprouted scythe tree grows large enough to be commanded. It makes a melee Strike against the target or a creature adjacent to the target, with a +18 to hit and dealing 1d10 slashing damage.

**Craft Requirements** The initial raw materials must include branches and roots from a scythe tree.

**Source:** `= this.source` (`= this.source-type`)
