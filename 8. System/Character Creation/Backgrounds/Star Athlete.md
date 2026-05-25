---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Games Lore Lore"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whatever the sport, be it basilisk, kickball, wrestling, footraces, stickball, canoeing, or foot volleyball, you either have played it or are keen to try it. You probably missed some classes due to practice or competitions, and irate professors might dismiss you as lazy or incapable of learning. These assumptions ignore the countless hours you've dedicated to athletic excellence.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in Athletics. You're also trained in the Games Lore skill or a Lore skill associated with your school. You gain the [[Assurance]] skill feat with Athletics.

**Source:** `= this.source` (`= this.source-type`)
