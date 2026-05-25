---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Dragon]]"]
hp: "8"
size: "Tiny"
speed: "20"
boosts: "Dex, Cha, Str/Dex/Con/Int/Wis/Cha"
flaws: "Con"
languages: "Common, Draconic"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Dragonets are miniature dragons, complete with wings, dagger-like teeth, and magical breath. They can be fiercely independent and proud, at times protective or avaricious, and they delight in the finer things in life.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
