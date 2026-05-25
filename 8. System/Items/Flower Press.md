---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 6}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A flower press resembles a book with wooden covers and straps that tighten down to apply pressure. There are individual pages for multiple plants. Pressing flowers and other plants in this way allows them to be preserved for future study or as ornamentation. It can also be used to make impressions of plants for inclusion in journals and guidebooks instead of illustrations. Most flower presses can contain a dozen or so flowers at a time, each one on a different layer.

**Source:** `= this.source` (`= this.source-type`)
