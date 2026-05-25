---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 5}"
usage: "affixed-to-firearm"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a firearm

**Activate** `pf2:f` (concentrate)

**Requirements** You're wielding the affixed firearm.

This tiny copper gear is attached to the side of a firearm with a matching bolt or pin. When you activate it, the affixed weapon magically transfigures itself into the form of any simple or martial firearm to which you have access, harmlessly ejecting any contained ammunition in the process. Any runes or attached items present on the affixed weapon remain active unless incompatible with its new form, in which case they're suppressed for the duration of the transformation. The effect lasts until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
