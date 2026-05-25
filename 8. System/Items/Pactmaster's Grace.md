---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 4000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Granted by Katapesh's Pactmasters to influential merchants, exceptional Zephyr Guards, and favorite retainers, a pactmaster's grace is a crystal-studded blue platinum ring that sharpens the wearer's urban instincts. While invested, the ring grants a +2 item bonus to saving throws while you are in an urban setting, and this increases to a +3 item bonus if you have legendary proficiency in Guild Lore, Katapesh Lore, Mercantile Lore, or Society. You also gain a +3 item bonus to Mercantile Lore checks while wearing the ring, and you can attempt checks that require a proficiency rank of master in Society.

**Source:** `= this.source` (`= this.source-type`)
