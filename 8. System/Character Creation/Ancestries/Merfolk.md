---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Amphibious]]", "[[Humanoid]]", "[[Merfolk]]"]
hp: "8"
size: "Medium"
speed: "5"
boosts: "Dex, Cha, Str/Dex/Con/Int/Wis/Cha"
flaws: "Con"
languages: "Common, Thalassic"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Merfolk live in every ocean of Golarion, infinite in their variety and awe-inspiring in their majesty. They consider themselves, not without some merit, the rulers of the sea. Among the tropical reefs of the Fever Sea, merfolk build temples and palaces of brightly colored corals. Beneath the ice floes of the Shining Sea, merfolk hunt seals and whales for food in small, standoffish clans. In the Embaral Ocean, merfolk populate the great trading city of Alohmab, built into the shell of a titanic snail that crawls across the ocean floor.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
