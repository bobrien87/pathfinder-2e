---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Focused]]", "[[Invested]]"]
price: "{'gp': 1000}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gauzy purple veil is embroidered with symbols of divinatory significance. As your curse worsens, the veil ripples in an ever-increasing unseen wind. You gain a +2 item bonus to Religion checks.

**Activate—Remember the Future** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a revelation spell. If you don't spend this Focus Point by the end of this turn, it's lost.

**Activate—Twist the Skeins of Fate** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** An ally within 30 feet is about to attempt a saving throw

**Requirements** You have the [[Cursebound]] condition

**Effect** The ally gains a status bonus to the saving throw equal to the value of your cursebound condition.

> [!danger] Effect: Twist the Skeins of Fate

**Craft Requirements** You're an oracle.

**Source:** `= this.source` (`= this.source-type`)
