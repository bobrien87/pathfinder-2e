---
type: item
source-type: "Remaster"
level: "0"
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Upon your brow is a gem that houses your soul. When casting any spell or ritual to return you to life, your intact head gem can be substituted for your body. While you can freely remove your head gem, it's typically impossible for another creature to forcibly remove or destroy your head gem unless you're killed or permanently incapacitated first; at the GM's discretion, powerful magic or abilities can circumvent this restriction. If your head gem is removed or destroyed, it can be regrown using a day-long ritual. When this occurs, any remains of the previous gem immediately crumble to dust.

**Source:** `= this.source` (`= this.source-type`)
