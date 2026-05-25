---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d8]]", "[[Parry]]"]
price: "{'gp': 5}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

As the name implies, a shield bow is a bow with an integrated shielding surface. While versatile and effective, a shield bow's architecture limits its flexibility somewhat, decreasing its total draw strength and penetrating power.

**Source:** `= this.source` (`= this.source-type`)
