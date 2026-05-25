---
type: ancestry
source-type: "Remaster"
rarity: "Uncommon"
traits: ["[[Humanoid]]", "[[Shadow]]", "[[Wayang]]"]
hp: "8"
size: "Small"
speed: "25"
boosts: "Dex, Cha, Str/Dex/Con/Int/Wis/Cha"
flaws: "Con"
languages: "Common, Shadowtongue, Wayang"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Wayangs are diasporic sojourners from the Netherworld where they lived and worked alongside their allies, lightweaving d'ziriaks. Both peoples shared affinities for artistic expression and spiritual introspection, inspiring each other's sensitivities to color, form, and function; they also bolstered each other's defense against rampaging dragons, oni, and undead. This idyll collapsed from divine meddling; some say when Abadar sentenced Zon-Kuthon to exile in the Netherworld, the Midnight Lord's deific presence distorted the plane into a nightmarish domain, while others accounts ascribe fiendish sources to this doom.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
