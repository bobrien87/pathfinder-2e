---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Produced to promote plays, *illusory programs* are thin pamphlets infused with minor magic. Upon opening one of these pamphlets, readers are treated to a series of tiny illusions that stand on each page, typically showcasing highlights of the performance or profiles of the cast. The magic woven into each page is of the cheap, short-lived variety, fading 24 hours after the program has been opened.

**Source:** `= this.source` (`= this.source-type`)
