---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have been blessed by a divinity. For an unknown reason, and irrespective of your actual beliefs, a deity has granted you a boon to use for good or ill. Your blessing grants wisdom and insight to aid you in your struggles. You may or may not even know the identity of the being who blessed you, and the blessing might come with a cost you discover later on.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You are trained in a Lore skill associated with the deity who blessed you (such as Shelyn Lore) if you know their identity, or else in a Lore skill of the GM's choice if you don't. Either you can cast [[Guidance]] as a divine innate spell at will, or you gain a similar blessing determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
