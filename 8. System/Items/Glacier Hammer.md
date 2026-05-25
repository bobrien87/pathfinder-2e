---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Shove]]"]
price: "{'gp': 60}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Frost covers the head of this *+1 magic maul*. Any hit with this maul deals 1 extra cold damage. You can use a special action to transform the frost into giant icicles.

**Activate—Grow Icicles** `pf2:1` (concentrate) Until the end of your turn, the maul deals 1d6 extra cold damage instead of just 1. After you activate the glacier hammer, you can't activate it again for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
