---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 200}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You're targeted with an attack but the opponent hasn't rolled yet.

These wooden discs sometimes form spontaneously at the Wood Pile, a secret conrasu location suffused with extraplanar energy. A conrasu coin can be activated to call upon the power of a specific type of aeon.

This cog-like coin bears an hourglass on one side and the four-armed silhouette of a bythos—aeons that steward over time—on the other. When activated, you catch a glimpse of your body moving on one of its potential timelines in response to danger and you follow those movements to dodge. You gain a +2 circumstance bonus to AC against the attack, and after resolving the attack, you can Stride up to 10 feet without triggering reactions. If you have the Nimble Roll feat and the attack misses, you can Stride up to 20 feet instead.

**Source:** `= this.source` (`= this.source-type`)
