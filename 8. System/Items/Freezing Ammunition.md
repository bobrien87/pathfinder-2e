---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Cold]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 25}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This chilly ammunition is dark blue and cold to the touch. When activated *freezing ammunition* hits a target, the target must succeed at a DC 19 [[Fortitude]] save or be [[Slowed]] 1 for 1 round by the intense cold (slowed 1 for 1 minute on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
