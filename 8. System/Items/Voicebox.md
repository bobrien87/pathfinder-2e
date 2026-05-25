---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'sp': 5}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This box contains small, magical amplifiers that allow a non-verbal character to translate thought into speech, which emits from the necklace. The speech produced matches any language you understand.

**Source:** `= this.source` (`= this.source-type`)
