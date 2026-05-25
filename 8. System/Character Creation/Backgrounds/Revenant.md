---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion, Boneyard Lore Lore"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You died. No real doubt about that. Bullet to the brain or knife to the throat, you were dead as dead can be. Then you got back up again. Maybe you had some unfinished business, or maybe you were just so tough and so mean that Hell itself spat you out. Either way, you came back for a reason.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in Religion and Boneyard Lore. You're still alive, not undead, but you have the void healing ability, which means you're harmed by vitality damage and healed by void effects as if you were undead.

**Source:** `= this.source` (`= this.source-type`)
