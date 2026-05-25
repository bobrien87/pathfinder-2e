---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Companion]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 475}"
usage: "worncollar"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This leather collar's worn and almost threadbare look belies its magical nature. When your companion wears and invests the collar, it gains the ability to change its appearance from that of a ferocious animal into a more inconspicuous form.

**Activate—Adorable Guise** A envision

**Effect** You touch your animal companion to transform it into a nonthreatening Tiny creature of the same family or a similar creature (for instance, a house cat instead of a tiger, or a puppy instead of a wolf). This has the effects of [[Pest Form]] (2nd rank, or 4th rank if your companion can fly). The effect lasts until you Dismiss it.

**Source:** `= this.source` (`= this.source-type`)
