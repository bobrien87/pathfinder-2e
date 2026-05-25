---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 3000}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This moderate reinforcing steel shield (Hardness 8, HP 84, BT 42) has an image of a cinder dragon's head painted on it. Additional metal adornments accentuate the fearsome mouth.

**Activate—Burning Path** `pf2:3` (fire, manipulate)

**Frequency** once per day

**Effect** You Raise your Shield and Stride up to twice your Speed in a straight line. You can move through creatures with this movement, but you can't end your movement in their space. Creatures you moved through take 5d8 fire damage (DC 31 [[Reflex]] save). Creatures who critically fail also take 1d8 persistent,fire damage.

**Source:** `= this.source` (`= this.source-type`)
