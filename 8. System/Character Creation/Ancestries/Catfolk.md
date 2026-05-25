---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Catfolk]]", "[[Humanoid]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Cha, Dex, Str/Dex/Con/Int/Wis/Cha"
flaws: "Wis"
languages: "Amurrun, Common"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Curious and gregarious wanderers, catfolk combine the features of felines and humanoids in both appearance and temperament. They enjoy learning new things, collecting new tales and trinkets, and ensuring their loved ones are safe and happy. Catfolk view themselves as the chosen guardians of natural places in the world and are often recklessly brave, even in the face of overwhelming opposition. They believe that strong communities, breadth of experience, and continual self-improvement aid them in this fight.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
