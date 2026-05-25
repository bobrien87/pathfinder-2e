---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Trip]]"]
price: "{'gp': 240}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking kukri* has a crimson blade that shimmers eerily in bright light. On a critical hit, the kukri deals 1d8 persistent bleed damage. If the target didn't already have persistent bleed damage when you scored the critical hit, you also gain `r 1d8` temporary Hit Points for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
