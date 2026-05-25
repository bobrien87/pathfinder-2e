---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Herbalism Lore Lore"
feats: "[[Root Magic]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Some ailments can't be cured by herbs alone. You learned ritual remedies as well, calling on nature spirits to soothe aches and ward off the evil eye. Taking up with adventurers has given you company on the road, as well as protection from those who would brand you a fake—or worse.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Occultism skill and the Herbalism Lore skill. You gain the [[Root Magic]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
