---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Lizardfolk]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Str, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Int"
languages: "Common, Iruxi"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Lizardfolk are consummate survivors, heirs to empires considered ancient even by the elves.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
