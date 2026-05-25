---
type: item
source-type: "Remaster"
level: "4"
price: "{'gp': 75}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Usually worn by actors but also popular with anyone intent on subterfuge, this outfit resembles a normal piece of clothing, but with multiple pockets designed to conceal blood pack squibs and similar small items. When wearing this outfit, you automatically succeed on all relevant checks to Conceal an Object on your person as long as the object is of light or negligible Bulk. However, someone specifically searching you can still attempt a Perception check against your Stealth DC.

**Source:** `= this.source` (`= this.source-type`)
