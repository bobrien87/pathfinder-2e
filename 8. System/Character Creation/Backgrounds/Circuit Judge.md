---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Deception, Legal Lore Lore"
feats: "[[Lie To Me]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're a circuit judge, a courtroom on horseback who serves a group of communities out in the Mana Wastes or a similar backwoods region. You show up every couple of months, hear the cases that have piled up since your last visit, give verdicts, and then it's on to the next town in your itinerary. It's not the easiest life in the world, but it's an interesting one, and you hear some mighty strange cases. Chances are, it was one of those cases that set you on the road to adventure.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in Deception and Legal Lore. You gain the [[Lie to Me]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
