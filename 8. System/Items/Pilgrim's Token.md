---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "other"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden religious symbol is a small token of protection from a site holy to your faith. As long as this religious symbol is in your possession, when you tie an adversary's initiative roll, you go first.

If you lose this religious symbol, you must purchase or Craft a replacement and attune it. Such a token usually costs at least 1 sp, and the attunement takes 10 minutes of prayer. You can also attune a different religious symbol with the same amount of time, but you lose the benefit of the previous religious symbol.

**Source:** `= this.source` (`= this.source-type`)
