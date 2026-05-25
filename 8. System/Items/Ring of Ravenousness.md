---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 325}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved of acacia wood, a ring of ravenousness is inlaid with a geometric pattern. The ring appears to be a *[[Ring of Sustenance]]*. Once you invest it, though, it fuses to you, its effects activating immediately. While wearing the ring, you require twice the normal amount of food and drink for a creature your size to avoid starvation and thirst.

**Source:** `= this.source` (`= this.source-type`)
