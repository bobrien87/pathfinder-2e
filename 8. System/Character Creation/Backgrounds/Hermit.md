---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
feats: "[[Dubious Knowledge]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

In an isolated place—like a cave, remote oasis, or secluded mansion—you lived a life of solitude. Adventuring might be a welcome reprieve from solitude or an unwanted change, but in either case, you're likely still rough around the edges.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in the Nature or Occultism skill, plus a Lore skill related to the terrain you lived in as a hermit (such as Cave Lore or Desert Lore). You gain the [[Dubious Knowledge]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
