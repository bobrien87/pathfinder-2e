---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Performance, Fireworks Lore Lore"
feats: "[[Fascinating Performance]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Few celebrations in Tian Xia are complete without a show of fireworks, and your job is to make sure they go off without a hitch. You load the fireworks, set the fuses, and choreograph the performance, bringing the show together in a finale of lights and explosions. Then it's time to pack up your gear and move on to the next civic holiday or religious festival. Of course, someone who travels the roads with a pack full of high explosives is bound to run into an adventure or two along the way, and so over time, your fireworks have been spent in support of that life.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Performance skill and the Fireworks Lore skill. You gain the [[Fascinating Performance]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
