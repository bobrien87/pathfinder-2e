---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Fire]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 100, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner shimmers in a fiery array of reds, oranges, and yellows. The rampant threads catch light in the wind and give the appearance of a blazing flame. Whenever you or an ally within the banner's aura critically succeeds with a Strike, the Strike deals an additional 1d4 persistent,fire damage.

**Source:** `= this.source` (`= this.source-type`)
