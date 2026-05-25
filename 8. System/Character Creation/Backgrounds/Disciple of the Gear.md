---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting"
feats: "[[Quick Repair]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While many regard science and faith as incompatible, you believe scientific advancement is your deity's will. Perhaps you're a follower of Brigh, Casandalee, or some other god of technology, or perhaps you see the furnaces and sparks of modernity as the latest manifestation of Sarenrae's flame or Gozreh's lightning—whatever the case, you're always willing to spread the word of your deity, and you've learned some basic tinkering to show how your deity's focus can increase the common standard of living.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Crafting skill and the Lore skill for the deity you worship. You gain the [[Quick Repair]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
