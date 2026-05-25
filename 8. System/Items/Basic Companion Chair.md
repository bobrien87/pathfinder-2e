---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Barding]]", "[[Companion]]"]
price: "{'sp': 4}"
usage: "other"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This harness fits around the torso of an animal companion and connects via struts to a number of wheels to assist the companion's movement. Companion chairs can be fitted for animal companions of any shape or size and have two- and four-wheel configurations. Like the basic chair, a companion chair is ideal for everyday use but not more strenuous activity, making it more common among non-adventurers.

**Source:** `= this.source` (`= this.source-type`)
