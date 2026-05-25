---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 85, 'pp': 0, 'sp': 0}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you put on this belt, its silver buckle begins to glow, which slowly spreads into the heart-shaped jewel in the center. You increase your maximum Hit Points and current Hit Points by 4. If you remove the belt, you immediately decrease both your maximum and current HP by 4.

**Source:** `= this.source` (`= this.source-type`)
