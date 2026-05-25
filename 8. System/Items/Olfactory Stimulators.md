---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]"]
price: "{'gp': 5}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cluster of sensitive wire whiskers fits over the nose or snout to provide sensory information as it reacts to nearby odors and other scents. A creature wearing olfactory stimulators gains a sense of smell, which is as precise as an average member of its species, as well as the scent special ability if members of its species typically have that ability. Olfactory stimulators can be fitted to animal companions as well as sapient creatures; stimulators produced for companion use have the companion trait.

**Source:** `= this.source` (`= this.source-type`)
