---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
bulk: "2"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 adamantine scale mail* appears to have a *fortification* rune but grants none of its effects. Whenever you are critically hit, after taking damage, you become petrified for 1 round. Once the curse has activated for the first time, the armor fuses to you.

**Source:** `= this.source` (`= this.source-type`)
