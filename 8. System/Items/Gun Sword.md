---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Combination]]", "[[Concussive]]", "[[Kickback]]"]
price: "{'gp': 13}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon consists of a large sword with a powerful gun based on a harmona gun down the center. Vanguards and other characters who rely on Strength and Dexterity enjoy the power and flexibility of a gun sword.

**Source:** `= this.source` (`= this.source-type`)
