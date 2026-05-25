---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Force]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 4500}"
usage: "wornarmbands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Decorated with clear gemstones, these thick metal bands spread an inflexible layer of force over your body. The force grants you a +2 item bonus to AC and saving throws, and a maximum Dexterity modifier of +5 as armor. You can affix talismans to the bands as though they were light armor.

**Activate—Return Force** R (force, manipulate)

**Trigger** A creature critically misses you with a melee Strike

**Effect** You Shove the creature using the bands' Athletics modifier of +21.

**Source:** `= this.source` (`= this.source-type`)
