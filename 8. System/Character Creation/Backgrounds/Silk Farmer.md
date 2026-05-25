---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Sericulture Lore Lore"
feats: "[[Specialty Crafting]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

**Access** Tian Xia origin

You've studied and mastered the art of sericulture. The cultivation of silkworms to produce silk is an important industry that requires an intense amount of study and care. The unchanging routine of a silk farmer could make any adventure an epic one by comparison, and perhaps that prospect led you toward adventuring.

Choose two attribute boosts. One must be to **Wisdom** or **Intelligence**, and one is a free attribute boost.

You're trained in Crafting skill and Sericulture Lore. You gain the Specialty Crafting skill feat.

**Source:** `= this.source` (`= this.source-type`)
