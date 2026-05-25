---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Goblin]]", "[[Reach]]", "[[Trip]]", "[[Versatile p]]"]
price: "{'sp': 9}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Created by goblins to battle horses, this weapon is essentially a long shaft ending in a blade with a large hook.

**Source:** `= this.source` (`= this.source-type`)
