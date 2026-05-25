---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Kholo]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Str, Int, Str/Dex/Con/Int/Wis/Cha"
flaws: "Wis"
languages: "Common, Kholo"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Kholo have bad reputations as brutal raiders and demon-worshipers. Many believe that kholo are witches, cannibals, and worse. The truth is more complex. Kholo are eminently practical and pragmatic hunters and raiders. To them, honor is just another word for pointless risk. Any loss of a kholo affects not just the individual, but their packmates and kin as well. Wasting time on anything but victory, whether it's mercy or cruelty, is seen as little shy of immoral. Kholo are masters of ambushes, tactical feints, and psychological warfare. Equally misunderstood is the kholo practice of ancestor worship and endocannibalism. Kholo consume their dead as a sign of reverence, holding a grand feast and transforming the bones into art or weapons. Kholo extend this honor to respected foes, hoping to bring their enemy's cunning or strength into the clan.*

*

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
