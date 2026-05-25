---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Heraldry Lore or Warfare Lore Lore"
feats: "[[Armor Assist]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You trained at the feet of a knight, maintaining their gear and supporting them at tourneys and in battle. Now you search for a challenge that will prove you worthy of full knighthood, or you've spurned pomp and ceremony to test yourself in honest, albeit less formal, combat.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Athletics skill and your choice of the Heraldry Lore or Warfare Lore skill. You gain the [[Armor Assist]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
