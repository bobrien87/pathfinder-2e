---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Propulsive]]", "[[Tengu]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tengu use these specialized slings to fire darts further and with greater force than when thrown by hand. A thunder sling uses darts as ammunition. It can also hurl blowgun darts as ammunition but deals @Damage[(1d4)[piercing]] damage instead of 1d6 when used this way.

**Source:** `= this.source` (`= this.source-type`)
