---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden box unfolds into a stack of hinged trays holding calipers, magnifying lenses, acids and reagents, comparison sketches of species commonly mistaken for one another, and glass slides for specimen testing. When you use this kit to study accounts of a creature or what it left behind (such as spoor, tracks, or fur samples), you gain a +1 item bonus to [[Recall Knowledge]] about the creature or to `act track` the creature. In addition, if you fail to Recall Knowledge about the creature (but don't critically fail), you're able to eliminate at least one possibility of a common type of animal. For instance, you might be able to verify the creature isn't an ankhrav, even if you get no further information.

**Source:** `= this.source` (`= this.source-type`)
