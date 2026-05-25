---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Nature, Herbalism Lore Lore"
feats: "[[Natural Medicine]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

As a formally trained apothecary or a rural practitioner of folk medicine, you learned the healing properties of various herbs. You're adept at collecting the right natural cures in all sorts of environments and preparing them properly.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Nature skill and the Herbalism Lore skill. You gain the [[Natural Medicine]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
