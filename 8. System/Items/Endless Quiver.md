---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "worn"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Elite archers can go through countless arrows over the course of a battle. Smart ones carry an endless quiver to ensure they never run out. This quiver holds 40 mundane arrows and regenerates 10 per hour. Once an arrow is removed from the endless quiver, it dissipates after 1 minute.

**Activate—Convert Arrows** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You tap the quiver, and the arrows inside transform into cold iron or silver. They revert to wood after 1 minute.

> [!danger] Effect: Convert Arrows

**Source:** `= this.source` (`= this.source-type`)
