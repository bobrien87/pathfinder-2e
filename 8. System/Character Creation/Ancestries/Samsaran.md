---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Samsaran]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Con, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Cha"
languages: "Common, Samsaran"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Samsarans, as the tale goes, originated with a group of scholars in Zi Ha who ventured into the mountains to find the cure for an illness ravaging their village. After weeks of peril, they found a freshwater spring filled with pure magical life essence. This water brought the scholars back from the brink of death and cured the villagers. Given a new chance at life, everyone who drank the water devoted the rest of their life to learning and experiencing the world fully. Upon death, this devotion, combined with the magical essence now infused in their bodies, transformed these people into the first samsarans.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
