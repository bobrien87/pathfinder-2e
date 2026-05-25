---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Games Lore Lore"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Eventually, even the greatest hero-god must die. Yet many live eternally through song, poetry, shrines, and art. Even though Iblydos isn't producing new hero-gods, its people know how to appreciate and commemorate a real hero. You hope to seize that same immortality through exceptional deeds and a little luck. If everything goes to plan, you'll retire rich and famous, looking good all the while. If the fates turn against you, at the very least you know tales of your exploits will dazzle audiences for ages.

Choose two attribute boosts. One must be to **Strength** or **Charisma**, and one is a free attribute boost.

You're trained in either the Intimidation or Performance skill, as well as the Games Lore skill. If you choose Intimidation, you gain the [[Intimidating Glare]] skill feat. If you choose Performance, you gain the [[Impressive Performance]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
