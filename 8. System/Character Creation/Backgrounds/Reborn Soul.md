---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were given a second opportunity at life by mysterious forces in the Lands of Second Souls. You remember your life before your death and now live with an extra lifetime of knowledge.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You become trained in two Lore skills, which you and your GM choose from Lore skills associated with your past life. At 3rd level, 7th level, and 15th level, you receive skill increases, which you can apply only to these Lore skills. In certain situations analogous to your past life, fragments of memories resurface, potentially helping or distracting you. The GM can offer you a +1 circumstance bonus on skill checks with either of these Lore skills or on other skill checks that echo your past life. If you accept but fail the check, you're [[Stupefied 1]] for 1 minute by the mental distraction of your past-life memories, or [[Stupefied 2]] for 1 minute on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
