---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Nature, Plane of Earth Lore Lore"
feats: "[[Natural Medicine]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Mineral formations can be beautiful things, sparkling and arrayed in geometric configurations. To you, they are also potent natural healing aids. You may have taken up adventuring to prove yourself by healing the ailing or to find new crystals with unique properties to add to your growing collection.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma** and one is a free attribute boost.

You're trained in the Nature skill and the Plane of Earth Lore skill. You gain the [[Natural Medicine]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
