---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Amphibious]]", "[[Athamaru]]", "[[Humanoid]]"]
hp: "8"
size: "Medium"
speed: "20"
boosts: "Str, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Int"
languages: "Common, Thalassic"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Athamarus are fish-like humanoids who form tight-knit undersea communities. In small settlements, they engage in the subsistence farming of seaweed, train eels to serve as mounts, and create elaborate works of coral art. Their interactions with other aquatic ancestries are strained, as athamarus have suffered mistreatment at their hands. However, they remain curious about potential connections and what new opportunities may offer.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
