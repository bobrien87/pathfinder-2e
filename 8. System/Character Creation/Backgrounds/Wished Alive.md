---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Once you were a simple construct or inanimate doll, but due to a deeply felt wish, either yours or another's, you came to life, and so you're now a living, breathing creature.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in the Diplomacy skill. Once per day, you can fervently wish for something you could work towards achieving as a single action which has the concentrate trait. If you do, you gain a +2 circumstance bonus on the first skill check you attempt before the end of your turn to fulfill that wish.

**Source:** `= this.source` (`= this.source-type`)
