---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Divine]]", "[[Invested]]"]
price: "{'gp': 360}"
usage: "worn"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Requirements** You're a follower of Urgathoa.

This finger-shaped crystal on a thin strip of leather bridges the worlds of life and undeath, shifting from a pale opaque pink when worn by a living creature to a deep translucent purple when worn by an undead creature. While wearing the necklace, rotten food and drink taste as if they were fresh and can be eaten with no ill effects. If you're healed by healing vitality effects, you gain void resistance 5, but if you're healed by void effects, you instead gain vitality resistance 5.

**Source:** `= this.source` (`= this.source-type`)
