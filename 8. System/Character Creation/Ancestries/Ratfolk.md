---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Ratfolk]]"]
hp: "6"
size: "Small"
speed: "25"
boosts: "Dex, Int, Str/Dex/Con/Int/Wis/Cha"
flaws: "Str"
languages: "Common, Ysoki"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Ysoki are beings that most surface-dwelling humanoids refer to as "ratfolk." They are a communal people who prefer cramped conditions, with up to 100 individuals living in a given home. If they can't find homes in town, ratfolk may instead live in caves and cavern complexes, as these provide great storage for the many and varied goods they bring back from trading expeditions.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
