---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Deathstalk mushrooms that have been alchemically treated into this poison cause those who succumb to suffer horrific hallucinations in which everyone around them distorts into demonic shapes shortly before their own bodies begin to break down and melt from within. Creatures with the fungus trait are immune to this poison and often find the flavor of a deathstalk mushroom to be rather pleasant.

**Saving Throw** DC 35 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** [[Stupefied 1]] (1 minute)

**Stage 2** [[Confused]] and [[Stupefied 2]] (1 minute)

**Stage 3** 16d6 poison damage, confused, and [[Stupefied 3]] (1 minute)

**Stage 4** 17d6 poison damage, confused, and [[Stupefied 4]] (1 minute)

**Source:** `= this.source` (`= this.source-type`)
