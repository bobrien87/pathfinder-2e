---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Shove]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 4200}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking khakkhara* is topped by an ornate finial depiction of a small-statured traveler with animal companions. While the rings of a khakkhara are normally meant to alert others of one's presence, the magic of the *worldringer* enhances the chimes to entreat upon those who hear it.

**Activate—Chimes of Command** `pf2:3` (manipulate)

**Frequency** once per day

**Effect** You call upon beings of this plane or another to hear your call. Choose [[Summon Lesser Servitor]] or [[Command]]. You Cast the chosen Spell at 5th rank (DC 33). When casting *summon lesser servitor* in this way, you must choose to summon a magical animal.

**Source:** `= this.source` (`= this.source-type`)
