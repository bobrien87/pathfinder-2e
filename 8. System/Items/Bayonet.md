---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Attached to crossbow or firearm]]", "[[Finesse]]"]
price: "{'sp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This blade or spike can be attached to a crossbow or firearm but, unlike other attached weapons, can be wielded in one hand as its own weapon. When used as a separate weapon, it can't benefit from any runes or abilities that function only for attached weapons.

**Source:** `= this.source` (`= this.source-type`)
