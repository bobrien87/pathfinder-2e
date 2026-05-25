---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Beast]]", "[[Centaur]]", "[[Humanoid]]"]
hp: "8"
size: "Large"
speed: "30"
boosts: "Str, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Cha"
languages: "Common, Fey"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Centaurs are proud nomads who range far and wide across their ancestral territories, protecting their lands from exploitation and intrusion. They are survivalists who forge tight bonds with family and community and stand firm in the face of danger. Many are skilled hunters, trackers, and warriors who do battle with bow, steel, and hooves. Brave and stubborn, they're willing to challenge even the fiercest foes and largest forces to protect their homes, kin, and the land within their domain.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
