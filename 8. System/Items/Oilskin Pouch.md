---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "worn"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Treated with oil and animal fats, the leather of this pouch is more resistant to water but is also stiffer. Many makers and travelers decorate their oilskin pouches with symbols of the ocean and sailing. Often used to store scrolls or other paper documents when a traveler knows they will be in an area of heavy rain or near water. While not entirely waterproof, an oilskin pouch seals with sturdy leather ties, allowing it to resist anything other than total submersion. Even completely underwater, it will protect its contents for up to 1 minute.

An oilskin pouch can protect up to 1 Bulk of items.

**Source:** `= this.source` (`= this.source-type`)
