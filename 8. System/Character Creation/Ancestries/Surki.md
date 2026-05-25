---
type: ancestry
source-type: "Remaster"
rarity: "Rare"
traits: ["[[Humanoid]]", "[[Surki]]"]
hp: "8"
size: "Medium"
speed: "25"
boosts: "Con, Str/Dex/Con/Int/Wis/Cha"
languages: "Common, Surki"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.rarity != null and this.rarity != "", "[[" + this.rarity + "]] ", "") + "[[" + this.size + "]] " + choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

**Base HP** `= this.hp`; **Size** `= this.size`; **Speed** `= this.speed` feet
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.flaws != null and this.flaws != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Attribute Flaws** " + this.flaws, "") + choice(this.languages != null and this.languages != "", choice(this.boosts != null and this.boosts != "" or this.flaws != null and this.flaws != "", "<br>", "") + "**Languages** " + this.languages, "")`

Surkis are an insectile species who subsist on the latent magic in the world around them. As a subterranean species native to the Darklands, surkis have rarely been seen on the surface, and always with long pauses between historical sightings. This is due to surkis' life cycle—long dormancies followed by so-called "generation digs," as they migrate great distances in response to happenings underground. The healing of the Worldwound initiated one of the largest such digs in their history, bringing surkis up into the caverns and passages of the Sarkoris Scar and emerging onto the surface for the first time in many years. Since their emergence, several small surki settlements have been established in secluded corners of Sarkoris, voraciously cataloging the wildlife, magics, and various other inhabitants of the area as they explore the alien environment of the surface.

#### Heritages
``` dataview
LIST
WHERE ancestry = this.file.link AND lower(type) = "heritage"
```

**Source:** `= this.source` (`= this.source-type`)
