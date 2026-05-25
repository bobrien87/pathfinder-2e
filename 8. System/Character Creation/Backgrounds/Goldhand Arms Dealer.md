---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Mercantile Lore Lore"
feats: "[[Group Impression]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're a dwarven agent of the Goldhand Lodge, a collection of dwarven merchants based out of Dongun Hold who seeks to sell guns far and wide. High King Anong Arunak hasn't expressed approval for such a method of distribution yet, but in the meantime you're still out and about, talking up your wares and occasionally providing visceral demonstrations of the overwhelming stopping power of your firearms. These demonstrations and sales have given you a taste for adventure, and the constant threat of piracy has convinced you of the importance of adventuring with a group.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in Diplomacy and Mercantile Lore. You gain the [[Group Impression]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
