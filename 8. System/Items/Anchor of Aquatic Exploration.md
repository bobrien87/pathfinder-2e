---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 690}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

No matter how often it's washed, the last crystals of salt rime never quite leave this pitted anchor. When you're holding the anchor of aquatic exploration, you can breathe underwater; however, you can't Swim, losing any Swim speed you have, automatically failing any Athletics checks to Swim, and so on. Instead, when you enter a body of water, you sink to the bottom at a rate of 25 feet per round and can move across the bottom at your normal Speed. You're protected from environmental effects of deep water such as pressure, cold temperatures, and any negative consequences of depressurization.

**Activate** 1 minute (manipulate)

**Frequency** once per day

**Requirements** You're underwater

**Effect** You spend one minute digging the anchor into the seabed, after which the anchor casts a [[Cozy Cabin]] spell, summoning a sunken ship instead of a cabin. The sunken ship is filled with breathable air.

**Source:** `= this.source` (`= this.source-type`)
