---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Humanoid]]", "[[Yaoguai]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Cha, Con, Str/Dex/Con/Int/Wis/Cha"
flaws: "Int"
languages: "Common"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Yaoguai usually begin as simple animals, plants, or objects before finding a way to awaken to sapience, becoming strange shapeshifting creatures in the process. Often originating from an infusion of ambient energy into their original form, yaoguai attain their powers through training their innate magic. Taking care not to expose their true appearance and nature, yaoguai of the same origins or species sometimes form enclaves in which they dedicate their lives to honing their powers or engaging in hedonistic pursuits—though the two aren't mutually exclusive. Yaoguai who lack a solid community, meanwhile, feel compelled to cultivate themselves until they transcend their origin, which might allow them to join society and experience a new kind of freedom.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
