---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Twin]]"]
price: "{'gp': 24000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+3 greater striking animated dawnsilver sawtooth saber* has many serrated edges and gleams blinding white in bright light.

If you're wielding Blood-Drinker in your other hand, increase *Fleshrender's* attack modifier to +32 instead of +24, and increase its fly Speed to 50 feet when you Set Free *Fleshrender*.

**Source:** `= this.source` (`= this.source-type`)
