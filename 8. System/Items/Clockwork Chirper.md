---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Clockwork]]", "[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple clockwork bird is no larger than a sparrow, designed to be wound up and perched on a tree branch or ledge. The Tiny clockwork remains immobile and silent until a Small or larger creature enters the square beneath its perch, at which point it springs into action. Once activated, it flies around making a loud chirping sound that can be heard up to 500 feet away. The bird then follows the creature that activated it for up to one hour or until it is destroyed, doing its best to stay just above the creature and out of reach, and continuing its string of loud chirps. The bird is an object with a Speed 10 feet, and a fly Speed of 25 feet. It has AC 15, Hardness 5, HP 10 (BT 5) and object immunities. Once broken, it can no longer fly. It can't attack or otherwise damage other creatures. After an hour has passed after its activation, the clockwork chirper falls into a pile of useless components.

**Source:** `= this.source` (`= this.source-type`)
