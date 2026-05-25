---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Nature"
feats: "[[Train Animal]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have always felt a connection to animals, and it was only a small leap to learn to train them. As you travel, you continuously encounter different creatures, befriending them along the way.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in the Nature skill and a Lore skill related to one terrain inhabited by animals you like (such as Plains Lore or Swamp Lore). You gain the [[Train Animal]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
