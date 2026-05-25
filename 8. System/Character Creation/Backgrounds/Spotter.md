---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Stealth, Scouting Lore Lore"
feats: "[[Terrain Stalker]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

An eye for detail, a sense for the wind, and a strong trust in your gut feelings. These qualities have set you apart from others when it comes to assisting a sharpshooter with setting up the perfect shot against their target. Elevation, velocity, and concealment-these are all vital factors that need to be considered to pull off a feat of true marksmanship, and no sniper would be able to function without an experienced spotter. Since your younger days, you've put your skills as a spotter to work as an adventurer. Whether you're taking your own shots now or spotting for others, your talents grant you an edge in an adventuring career.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in the Stealth skill and the Scouting Lore skill. You gain the [[Terrain Stalker]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
