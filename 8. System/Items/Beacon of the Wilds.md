---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 3800, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner lightens your feet and allows you to move adroitly. This banner is sometimes referred to as the marching flag. You and your allies ignore difficult terrain within the banner's aura.

**Source:** `= this.source` (`= this.source-type`)
