---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A spellbook holds the written knowledge necessary to learn and prepare various spells, a necessity for wizards (who typically get one for free) and a useful luxury for other spellcasters looking to learn additional spells. Each spellbook can hold up to 100 spells. The Price listed is for a blank spellbook.

**Source:** `= this.source` (`= this.source-type`)
