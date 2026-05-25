---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Acupuncture Lore Lore"
feats: "[[Battle Medicine]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

**Access** Tian Xia origin

You've studied qi and its abilities to heal the body through assessment and regulating qi flow. You know occult techniques that originated in Chu Ye before its masters were driven away when oni took over. You might have encountered a master willing to teach an eager student or felt the relief of its practice on your own body, taking your interest to greater heights.

Choose two attribute boosts. One must be to **Wisdom** or **Dexterity**, and one is a free attribute boost.

You're trained in Medicine and Acupuncture Lore. You gain the Battle Medicine skill feat.

**Source:** `= this.source` (`= this.source-type`)
