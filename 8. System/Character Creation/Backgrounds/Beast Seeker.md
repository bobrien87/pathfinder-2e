---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Legendary Beast Lore Lore"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

From jagged reefs to trackless forests to volcanoes dusted by snow even at this low latitude, Iblydos is home to fearsome creatures willing to eat civilians and snap ships in half. There might be no greater place to test one's monster-hunting credentials than this archipelago, much as countless hero-gods have done over the millennia. Perhaps you traveled here to learn how to slay leviathans and better defend your homeland from some bestial threat. You might instead value the esoteric properties of the slain creatures, knowing the alchemical potential of a hydra's eye or a medusa's venom. Whatever your motivation, you have honed tactics to trip and even tackle massive monsters.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in either the Athletics or Thievery skill, as well as the Legendary Beast Lore skill. If you choose Athletics, you gain the [[Titan Wrestler]] skill feat. If you choose Thievery, you gain the [[Dirty Trick]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
