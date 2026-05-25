---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Spirit]]", "[[Yaksha]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Con, Cha, Str/Dex/Con/Int/Wis/Cha"
flaws: "Int"
languages: "Common, Fey, Yaksha"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Away from shining citadels and opulent palaces, reticent yakshas shelter Tian Xia's rural hinterlands from natural disasters and otherworldly depredations. Famed for resolute vows and prowess with primal magic, yakshas shield the indigent and protect the wilderness, punishing those who threaten either with bone-crushing fury. Yaksha legends recall their origins as divine spirits, overseeing the safety of roads and abodes in a primeval world of vast storm forests and titanic flame floods—the First World, a realm of boundless potentiality. During the Great Abandonment, when the gods left the First World, many yakshas rejected this exodus, instead staying to perform their duties as caretakers. Despite the realm's sudden dearth of divine power, the remaining yakshas swore primordial vows, allowing them to channel power from the nearby Creation's Forge into primal magic and transform swathes of the metamorphic First World into stable regions to provide refuge for destitute fey.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
