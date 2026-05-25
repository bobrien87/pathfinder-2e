---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Underworld Lore Lore"
feats: "[[Risky Surgery]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're the medic many turn to when a more official clinic or healer might not be available. You may specialize in stitching up bullet wounds or have a standing, confidential deal with a criminal syndicate to provide your services any time of day or night. In either case, you've perhaps turned to the adventuring life because a former client is unhappy with your work or members of the local constabulary have been asking too many questions.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and the Underworld Lore skill. You gain the [[Risky Surgery]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
