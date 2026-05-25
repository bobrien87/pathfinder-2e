---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Fey Lore Lore"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have spent time in the First World or another realm of the fey and aren't entirely the same person you were before. Perhaps you made a purchase at the legendary Witchmarket or partook deeply of fey food and wine. Whatever the case, willingly or inadvertently, you made a bargain with the fey, the benefits of which come at a price.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You are trained in Fey Lore and gain the [[Fey's Fortune]] free action. You must follow some rule or limitation as part of your pact with the fey. If you violate the rule, you lose Fey's Fortune until you receive the effects of a successful [[Atone]] ritual using the Nature skill. The exact limitation is up to you and the GM, but the most common requirement is that you must fulfill a single request from any fey who knows your name.

**Source:** `= this.source` (`= this.source-type`)
