---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small wooden whistle bears an engraving with a symbol representing the word "query." Practitioners of kotodama magic use these whistles to speak with the spirits of objects.

**Activate—Question the Soul** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You place your hand on an object and play a single note on the whistle, causing the item to stir and respond to your questions for 1 minute. During this time, the object attempts to answer your questions to the best of its ability but can provide an answer of only "yes" or "no." In most cases, an object has knowledge only of events it was personally present for and has no particular knowledge skills to interpret the events it has seen. If the object can't answer a question with a simple yes or no answer, it stays silent.

**Source:** `= this.source` (`= this.source-type`)
