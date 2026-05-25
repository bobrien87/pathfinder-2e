---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Warfare Lore Lore"
feats: "[[Battle Medicine]]"
source: "Pathfinder Hellbreakers Player’s Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were an ordinary civilian until one day, Hellknights came to town and changed your world forever. You and your loved ones suffered under their brutality until liberation came, and now you have the chance to pay it forward as a Hellbreaker. As a hero

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and the Warfare Lore skill. You gain the [[Battle Medicine]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
