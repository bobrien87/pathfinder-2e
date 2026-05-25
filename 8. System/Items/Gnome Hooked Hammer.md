---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Gnome]]", "[[Trip]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gnome tool and weapon features a hammer at one end and a curved pick on the other. It's such a strange and awkward weapon that others think the gnomes are slightly erratic for using it.

**Source:** `= this.source` (`= this.source-type`)
