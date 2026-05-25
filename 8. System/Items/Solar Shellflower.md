---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Concussive]]", "[[Fatal d10]]"]
price: "{'gp': 160}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking flintlock musket* features multiple triangular panels that can be folded out of the stock, like the petals of a tigridia flower, that collect sunlight and feed it into the spark gun's core. All damage dealt by a *solar shellflower* is fire damage.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day (but see below)

**Effect** One of the panels from the *solar shellflower* detaches and unfurls into a tigridia-shaped construct of flame. For the next 1 minute, whenever you Strike an enemy with the *solar shellflower*, the construct fires a smaller jet of fire that automatically hits the target, dealing 3d4 additional persistent fire damage or twice that on a critical hit. The *solar shellflower* usually requires a full day to replenish enough solar energy to recharge this Activation, but if used in an environment with especially strong sunlight, such as in a desert, cliff above the clouds, or near the summer solstice, it can recharge in 1 hour instead.

**Source:** `= this.source` (`= this.source-type`)
