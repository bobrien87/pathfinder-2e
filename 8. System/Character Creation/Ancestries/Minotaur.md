---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Beast]]", "[[Humanoid]]", "[[Minotaur]]"]
hp: "10"
size: "Large"
speed: "25"
boosts: "Str, Con, Str/Dex/Con/Int/Wis/Cha"
flaws: "Cha"
languages: "Common, Jotun"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Minotaurs stalk complex passageways, whether natural or artificial, and are masters of stone architecture. Inquisitive and steadfast, these bovine humanoids spend their lives perfecting the pursuit that calls to them, which can sometimes lead them far from the enclaves where they were raised. Minotaurs are originally from the Iblydos archipelago but have spread far and wide across Golarion, forming close-knit communities often near mountains or beneath the surface of the earth. Though sometimes mistaken for simple brutes, minotaurs have scholars and warriors alike. Those who can look past their appearance will find an affinity for building and navigation, as well as creative problem-solving.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
