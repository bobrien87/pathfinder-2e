---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Agile]]", "[[Free hand]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This spiky, stony fragment shed from Ugly Cute's carapace fits comfortably over the hand. Though a little bulkier than the typical gauntlet, it still functions as a *+1 spiked gauntlet*.

**Activate—Ugly Cute's Favor** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You draw upon Ugly Cute's latent spiritual energy to infuse the gauntlet with forceful power. For 1 minute, Ugly Cute's gift gains the advantages of a [[Ghost Touch]] property rune and deals an additional 2 spirit damage on a successful Strike.

> [!danger] Effect: Ugly Cute's Gift

**Source:** `= this.source` (`= this.source-type`)
