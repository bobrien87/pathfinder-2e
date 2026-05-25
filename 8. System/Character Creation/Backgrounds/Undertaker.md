---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine"
feats: "[[Forensic Acumen]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

People die. This is the unfortunate fact of life on which you've founded your business, because wherever people die, there is a demand for mortuary services. You might be a Pharasmin priest or a secular professional, but your job is seeing to the body, comforting the bereaved, and making sure that the deceased goes to their ultimate reward with all due dignity. Of course, someone in your position sees a lot of strange deaths, and chances are one of them set you on the road to adventure.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and a Lore skill specializing in one local type of undead. You gain the [[Forensic Acumen]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
