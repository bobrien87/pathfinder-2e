---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 36000, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner is dip-dyed in an ombre from black to red, mottled and uneven. Whenever you or an ally within the banner's aura critically succeeds with a Strike against an [[Off Guard]] target, the Strike deals an additional 1d8 precision damage.

**Source:** `= this.source` (`= this.source-type`)
