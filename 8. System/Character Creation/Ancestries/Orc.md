---
type: ancestry
source-type: "Remaster"
traits: ["[[Humanoid]]", "[[Orc]]"]
hp: "10"
size: "Medium"
speed: "25"
boosts: "Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis"
languages: "Common, Orcish"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Orcs are forged in the fires of violence and conflict, often from the moment they are born. As they live lives that are frequently cut brutally short, orcs revel in testing their strength against worthy foes, whether by challenging a higher-ranking member of their community for dominance or raiding a neighboring settlement. Many orcs seek glory as soon as they can walk and carry a blade or club, taming wild beasts or hunting deadly monsters.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
