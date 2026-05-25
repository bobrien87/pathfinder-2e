---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]", "[[Void]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This black incense smells of fresh earth and ash. You activate the incense by lighting it, whereupon it fills a @Template[emanation|distance:10] with oily smoke and potent void energy. *Undead* creatures, including *incorporeal* undead, gain fast healing 4 while in the area; though this healing comes from void energy, it doesn't negatively impact living creatures. Once lit, the incense burns for 1 minute, and it can't be extinguished.

**Source:** `= this.source` (`= this.source-type`)
