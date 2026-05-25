---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "other"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This kit of bandages, herbs, and suturing tools is necessary for Medicine checks to [[Administer First Aid]], [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]]. If you wear your healer's toolkit, you can draw and replace its tools as part of the action that uses them.

**Source:** `= this.source` (`= this.source-type`)
