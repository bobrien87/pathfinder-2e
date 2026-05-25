---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "worn"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of a secret society

These braided wool cords are threaded with reflective metal threads in patterns specified by the purchaser. No two society's patterns are the same, and purchasers tend to return to the same weaver each time to ensure new cords match previous ones. In a room lit only by dim candlelight, the reflective metal threads shimmer in a specific pattern. Many societies use these cords to prevent outsiders from infiltrating secret meetings and often have someone at the meeting area's entrance checking cords before allowing entry.

**Source:** `= this.source` (`= this.source-type`)
