---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

You can apply snake oil onto a wound or other outward symptom of an affliction or condition (such as sores from a disease or discoloration from a poison). For the next hour, the symptom disappears and the wounded or afflicted creature doesn't feel as if it still has the wound or affliction, though all effects remain. A creature can uncover the ruse by succeeding at a DC 17 [[Perception]] check, but only if it uses a Seek action to specifically examine the snake oil's effects.

**Source:** `= this.source` (`= this.source-type`)
