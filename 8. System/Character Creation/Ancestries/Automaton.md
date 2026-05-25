---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Automaton]]", "[[Construct]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Str, Str/Dex/Con/Int/Wis/Cha"
languages: "Common, Utopian"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

These intelligent constructs house actual souls and represent what remains of a dying empire's last attempt at greatness. Automatons combine technological ingenuity with magical power, creating a blended being wholly unique to Golarion.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
