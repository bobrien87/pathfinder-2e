---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]"]
price: "{'gp': 16000}"
usage: "attached-to-crossbow-or-firearm-scope"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These scopes use magically enhanced lenses to extend the range of your weapon and help spot distant foes. The scope grants you a +3 item bonus to visual Perception checks to [[Seek]] creatures through the scope.

**Activate—Zoom In** `pf2:1` (manipulate)

**Effect** You zoom in on your targets to make it easier to hit them at a distance. You increase the range increment of the weapon to which the scope is attached by 20 feet until the beginning of your next turn or until you're no longer wielding the weapon, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
