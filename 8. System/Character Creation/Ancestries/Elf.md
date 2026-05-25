---
type: ancestry
source-type: "Remaster"
traits: ["[[Elf]]", "[[Humanoid]]"]
hp: "6"
size: "Medium"
speed: "30"
boosts: "Dex, Int, Str/Dex/Con/Int/Wis/Cha"
flaws: "Con"
languages: "Common, Elven"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

As an ancient people, elves have seen great change and have the perspective that can come only from watching the arc of history. After leaving the world in ancient times, they returned to a changed land, and they still struggle to reclaim their ancestral homes, most notably from terrible demons that have invaded parts of their lands. To some, the elves are objects of awe—graceful and beautiful, with immense talent and knowledge. Among themselves, however, the elves place far more importance on personal freedom than on living up to these ideals.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
