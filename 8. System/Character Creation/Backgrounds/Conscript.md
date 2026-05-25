---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Warfare Lore Lore"
feats: "[[Dubious Knowledge]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Like many others in your settlement, you readily performed your duty and served in the army once you came of age. Much to the chagrin of the grizzled lifers that sought to train it out of you, you managed to retain a modicum of your naivete even as you faced the gruesome horrors of war. You've learned just enough strategy and tactics to make you dangerous.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Society skill and the Warfare Lore skill. You gain the [[Dubious Knowledge]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
