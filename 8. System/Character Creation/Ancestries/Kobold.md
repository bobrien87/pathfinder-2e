---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Kobold]]"]
hp: "6"
size: "Small"
speed: "25"
boosts: "Cha, Dex, Str/Dex/Con/Int/Wis/Cha"
flaws: "Con"
languages: "Common, Sakvroth"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Every kobold instinctively understands the importance of power, and many are inclined to venerate those who have it, whether they be mighty dragons, cruel fiends, imperious fey, or even ancient artifacts. Kobolds seek out these alliances out of a sense of pragmatism—after all, who would dare bully a kobold who serves an ancient dragon?—but also because kobold eggs incubated near such loci of power take on physical traits (and sometimes abilities) similar to those of the warren's benefactor. On their own, kobolds are ingenious crafters and devoted allies, but outsiders who trespass into their territory find them to be inspired skirmishers and clever ambushers. However, these reptilian opportunists prove happy to cooperate with other humanoids when it's to their benefit, combining caution and cunning to make their fortunes in the wider world.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
