---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Clockwork]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Used by more technologically inclined bards, ventriloquists, and other performers to throw their voices, this gadget consists of two button-sized conch shells, each containing a miniaturized mechanism designed to pick up and transmit sound. One of the shells is designated the sending shell and contains a tiny indentation. When this indentation is pressed and the shell is close to a source of sound (such as on an actor's necklace), any sound that reaches it is transmitted to the receiver shell. If the receiver shell is located within 20 feet, it plays the sounds captured by the sending shell at a perfect volume and pitch.

**Source:** `= this.source` (`= this.source-type`)
