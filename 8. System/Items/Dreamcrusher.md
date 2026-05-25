---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 80}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The Order of the Rack uses weapons like the *dreamcrusher* to crush those who dare stand in the way. This *+1 longsword* has additional weight at the tip of its blade for the wielder to drive home their strikes.

**Activate—Doom the Rebel** `pf2:1` (concentrate, mental)

**Frequency** once per 10 minutes

**Requirements** Your last action was a Strike with the dreamcrusher that critically hit a creature

**Effect** The creature you critically hit must attempt a DC 19 [[Will]] save. On a failure, they take a –1 status penalty to attack rolls and skill checks for 1 round (1 minute on a critical failure).

> [!danger] Effect: Dreamcrusher

**Source:** `= this.source` (`= this.source-type`)
