---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Cursed]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made of a deep-brown rosewood, a *spurned lute* is adorned with carved flowers. The lute appears to be and functions as a virtuoso instrument. (Other *spurned instruments* exist, but the lute is the least rare.) This lute has a jealous streak, demanding total loyalty from its "partner" musician. After you play the lute for the first time, it fuses to you. If you go a day without using it to [[Perform]], you become [[Stupefied 1]] until you next do so. After that, when you attempt a Performance check using an instrument other than the lute, you take a –4 circumstance penalty to do so, and you must succeed at a DC 20 [[Will]] save or become stupefied 1 for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
