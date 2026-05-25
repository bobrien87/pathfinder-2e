---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Performance"
feats: "[[Impressive Performance]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've ridden a tornado, lassoed a river, mooned a dragon under a full moon, and shot six zombies with one bullet. That's what the stories say, anyway, and even if people don't strictly believe them, they are curious about you. Certainly, the stories keep spreading, and it would appear that you either have a unique destiny or are trying to convince the world that you do.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in Performance. You gain the [[Impressive Performance]] skill feat. You can gain the [[Leverage Connections]] skill feat later without being expert in Society or having Courtly Graces-this represents less traditional social connections and more the way that your legend has spread, and you've learned to leverage your legend, with people wanting to meet you and see you for themselves.

**Source:** `= this.source` (`= this.source-type`)
