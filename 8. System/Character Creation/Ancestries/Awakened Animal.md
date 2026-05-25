---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Awakened animal]]", "[[Beast]]"]
hp: "6"
size: "Medium"
speed: "5"
boosts: "Con, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Int"
languages: "Common"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

You once enjoyed the simple and boundless pleasures of nature with an innocent, uncluttered mind. You lived from moment to moment, never questioning what comes next or pondering the ramifications of what happened before. You were at one with the wild. Then came the event that changed everything. You drank from a glowing lake, someone pulled a magical prank, a druid sought to elevate your mind. You were pulled out of the present moment of the wild and into a land of thought.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
