---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Aura]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 2600}"
usage: "affixed-or-held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The warm, caring light of the sun glows from the center of this magical banner, mirroring the dawn. This magical banner exudes bright light in the banner's aura (and dim light in an area equal to twice the banner's aura). This effect is suppressed when you aren't holding the banner or wielding the weapon it is affixed to.

This magical banner also grants a +1 status bonus to saving throws against unholy effects to all creatures within the banner's aura.

**Source:** `= this.source` (`= this.source-type`)
