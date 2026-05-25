---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
usage: "applied-to-any-visible-article-of-clothing"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Common among brutes who use the magic to scare others into compliance, menacing runes lend you a formidable appearance, granting you a +2 item bonus to Intimidation checks to [[Coerce]] others.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The rune casts a 3rd-rank [[Fear]] spell (DC 25).

**Source:** `= this.source` (`= this.source-type`)
