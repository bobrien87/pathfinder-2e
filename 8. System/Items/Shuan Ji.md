---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backswing]]", "[[Forceful]]", "[[Reach]]", "[[Versatile p]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The shuan ji is a polearm featuring a long spear point on one end and two crescent-shaped blades that allow the wielder to strike with either side of the weapon.

**Source:** `= this.source` (`= this.source-type`)
