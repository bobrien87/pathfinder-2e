---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Artifact]]", "[[Cursed]]", "[[Divine]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This [[Immaculate Instrument]] has been cursed by the sublime breath it was taken from, causing it to warp, rust, or tarnish, though the holder of the instrument cannot perceive this and rationalizes away any attempt to explain the instrument's obviously cursed nature. Whenever the *cursed immaculate instrument* is used to produce a work, the holder must succeed on a DC 16 flat check or the work fails, leaving the holder frustrated and raising the DC of subsequent flat checks by 1. When the DC reaches 20, the work fails as normal, but the holder continues to attempt it fruitlessly to the exclusion of all other activities, including eating, drinking, and sleep, until they expire or the curse is broken.

**Source:** `= this.source` (`= this.source-type`)
