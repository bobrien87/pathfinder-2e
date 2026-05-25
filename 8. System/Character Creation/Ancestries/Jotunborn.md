---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Giant]]", "[[Humanoid]]", "[[Jotunborn]]"]
hp: "10"
size: "Large"
speed: "25"
boosts: "Str, Wis, Str/Dex/Con/Int/Wis/Cha"
flaws: "Cha"
languages: "Common, Jotun"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

According to their oldest stories, the first jotunborn were the direct creations of the earliest gods. Having just completed the majority of the creation of Golarion, these gods created several groups of people to act as stewards for this new world. Among these groups were jotunborn, beings who were formed from the remains of titans who dared rebel against the gods in the earliest days of existence. Rather than give jotunborn the full power they gave the titans, the gods instead instilled the first jotunborn with the faintest spark of creation and gave them slighter forms. These new servitors would be just as capable at helping to shape the rest of Golarion but would also be weaker and easier to strike down should they rebel like their progenitors.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
