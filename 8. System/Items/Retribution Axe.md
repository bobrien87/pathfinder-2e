---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Sweep]]"]
price: "{'gp': 60}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The blade of this *+1 greataxe* bears a design of a human skull.

Whenever a creature damages you with an attack, the skull changes its appearance to look like the face of that creature. You gain a +2 circumstance bonus to your next damage roll against that creature before the end of your next turn.

Because the face reshapes each time you're damaged, you get the additional damage only if you attack the creature that damaged you most recently.

**Source:** `= this.source` (`= this.source-type`)
