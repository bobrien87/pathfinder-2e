---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery, Underworld Lore Lore"
feats: "[[Pickpocket]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Some time ago, you stole a unique item from a strange individual. It might have been a piece of clockwork from a far-off land or some other bit of strange technology. You might still have it or you might have sold it, but either way, you can't shake the feeling that you're being followed and watched, likely by forces who want to retrieve what you took. Luckily, a life of adventure keeps you on the move.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in the Thievery skill and the Underworld Lore skill. You gain the [[Pickpocket]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
