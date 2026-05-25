---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 320}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You have a strong, prehensile tail. You gain a tail unarmed attack that deals 1d6 bludgeoning damage. This tail is in the brawling group. You gain a +1 item bonus to Acrobatics checks to [[Balance]] and to Athletics checks to Climb. You can also use your tail for the [[Grab an Edge]] action, even if your hands are otherwise occupied.

You can use your tail unarmed attack to [[Grapple]] even if you don't have a free hand. You gain a +2 item bonus to Athletics checks to Grapple.

**Source:** `= this.source` (`= this.source-type`)
