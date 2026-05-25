---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Tripkee]]"]
hp: "6"
size: "Small"
speed: "25"
boosts: "Dex, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Str"
languages: "Common, Tripkee"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Tripkees are a shy and cautious people who generally seek to avoid being drawn into the affairs of others. Despite their cautious outlook and small stature, adventurous tripkees still take bold and noble action when the situation demands it.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
