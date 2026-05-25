---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]", "[[Water]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Abhaya's tireless years of study have allowed her to reproduce, at some level, the unconscious melding of elements she experienced during the last Challenge of Sky and Heaven. A single drop of water in a crystalline container is the simplest application of her research.

When you activate this talisman, a watery echo of one of your limbs emerges from the container. Make a Strike with your fist or an unarmed attack from your ancestry. This attack gains the magical, reach, and water traits, retains any benefits from appropriate weapon fundamental runes (but not of weapon property runes), and takes no penalties for being used underwater. You can perform this Strike even if you're in a stance or under a polymorph effect that restricts your Strikes.

> [!danger] Effect: Drop of Convergent Waters

**Source:** `= this.source` (`= this.source-type`)
