---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Cursed]]", "[[Magical]]"]
price: "{'gp': 125}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A skull-topped metal *shrieking key* appears to be a *[[Skeleton Key]]*, useful in place of *Thieves' Tools* when attempting to Pick a Lock. A *shrieking key* has no activation, however. When you use it to Pick a Lock, the key emits a loud shriek audible for 500 feet despite ambient noise. Physical barriers still block or muffle the shriek as normal. You also take a –2 circumstance penalty to the Thievery check rather than enjoying a bonus. After you attempt such a check with the key the first time, it fuses to you, returning to your possession if discarded. To use another device to Pick a Lock, you must first succeed at a DC 20 [[Will]] save.

**Source:** `= this.source` (`= this.source-type`)
