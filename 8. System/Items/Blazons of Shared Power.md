---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 52}"
usage: "worn-and-attached-to-two-weapons"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These brass emblems come in a variety of designs, usually customized to the purchaser to reflect the heraldry of a family or guild. *Blazons of shared power* come in sets of three. When you invest the blazons, you wear one of the three on your chest, and you attach the others to a pair of one-handed weapons, choosing one as the primary weapon and one as the secondary weapon. These weapons can be either melee weapons or ranged weapons. As long as you're wielding both the primary weapon and the secondary weapon, the secondary weapon gains the benefit of the fundamental runes on the primary weapon. A weapon can only have a single blazon of shared power attached to it at a time.

**Source:** `= this.source` (`= this.source-type`)
