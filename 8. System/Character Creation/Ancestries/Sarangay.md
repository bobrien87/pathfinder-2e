---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Humanoid]]", "[[Sarangay]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Str, Cha, Str/Dex/Con/Int/Wis/Cha"
flaws: "Wis"
languages: "Common"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Sarangay are carabao-headed people who have long survived deep in the forests across Tian Xia. Many adventurers have thought them to be monsters at first, but sarangay are nothing more than a thriving society who value their community and their souls above all else. Their cultures are built upon the intense desire to protect their communities and their chosen leader. Their horns are said to be a crescent moon, and their towering statures are said to have come from their ancestors being stretched so far up to reach their Father Moon while their Mother Earth kept them close to her bosom. They revere the great Father Moon, their First Ancestor, and endeavor to protect and exalt nature above all else, for they understand that they're part of it.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
