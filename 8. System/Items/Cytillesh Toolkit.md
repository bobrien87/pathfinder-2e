---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "other"
bulk: "1"
source: "Pathfinder Monster Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These healer's toolkits are collections of crystalline scalpels and gritty salves made of cytillesh. They all glow the same sickly blue. While the toolkit is outside its opaque container, it sheds dim light in a 5-foot radius. Any non-dero using or wearing the toolkit is [[Sickened]] 1 until 1 hour after they've stopped, which cannot be reduced during that time.

**Source:** `= this.source` (`= this.source-type`)
