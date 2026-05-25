---
type: item
source-type: "Remaster"
level: "5"
price: "{'gp': 50}"
usage: "other"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Each war saddle is specifically fitted to a mount's body type and has numerous straps that can secure you on your mount. You remain mounted even if you fall [[Unconscious]] until either you or someone else uses an Interact action to unfasten the straps on the saddle. A creature or effect can separate you from your mount by pulling so hard it tears the straps, but to do so, the effect's DC, attack roll, or skill check must exceed 20.

**Source:** `= this.source` (`= this.source-type`)
