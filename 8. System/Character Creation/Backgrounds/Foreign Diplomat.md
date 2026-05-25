---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Heraldry Lore Lore"
feats: "[[Group Impression]]"
source: "Pathfinder Triumph of The Tusk Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have traveled a long way to be here, using your keen listening skills and careful words to make alliances that benefit your people and surgically sever ties that have become strained. You might be from Druma or Oprak, taking advantage of this invitation to forge new relationships, or you might be from the nations around Lake Encarthan and hoping to find an ally against Tar-Baphon.

Choose two attribute boosts. One must be to **Charisma** or **Constitution**, and one is a free attribute boost.

You're trained in the Diplomacy skill and the Heraldry Lore skill. You gain the [[Group Impression]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
