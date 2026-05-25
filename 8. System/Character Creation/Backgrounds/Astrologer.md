---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Astrology Lore Lore"
feats: "[[Oddity Identification]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Astrologers look to the stars for signs and portents, using their positions in the heavens to chart courses for those living beneath them. As the celestial spheres move, so does fate itself. You studied the stars and learned to divine your path based on their guidance. Whether the stars directly called you to a life of adventure or you use the stars to guide your wanderlust, you're living out the stars' guidance in a life of adventure.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in Occultism and Astrology Lore. You gain the [[Oddity Identification]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
