---
type: background
source-type: "Remaster"
boosts: "Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were once something supernatural—a heavenly agent, grim reaper, immortal phoenix, or demonic tyrant. For some reason, you've been forced to live in a mortal form. You might have been sealed by the holy power of a monk or cruelly betrayed and slain, but most likely, your superiors punished you for your hubris. You can't remember your previous life very well, if you're even aware you were once anything more than you currently are, but you aren't completely forsaken by the powers that once ruled your life. You often find a spark of enlightenment in failure, as fate nudges you to correct the mistakes or tragedies that caused your unmaking.

You gain two free attribute boosts. You choose one, and the GM chooses the other based on your past life.

You're trained in any one skill of your choice and any one Lore skill of your choice. You gain the [[Enlightenment in Adversity]] ability.

**Source:** `= this.source` (`= this.source-type`)
