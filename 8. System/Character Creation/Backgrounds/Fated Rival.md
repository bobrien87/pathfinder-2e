---
type: background
source-type: "Remaster"
boosts: "Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are bound in an adversarial relationship with another person or creature. You might have been close once, before everything went wrong, or they might have drastically altered your life at a crucial moment. Perhaps you are mystically bound by the red string of destiny, or perhaps your clash was preordained by the oracles of Po Li. Whatever the case, either fate or your own will keeps you driving forward to fight with them once more.

You and your GM work out who your rival is and how they fit in to your story. You become trained in two Lore skills related to your rival, which you and your GM choose.

You gain two free attribute boosts; you choose one, and the GM chooses one to complement your rival. So long as you are not in the presence of your rival, you gain the Diehard general feat and a +1 circumstance bonus to saving throws against the doomed condition. When in the presence of your rival, you lose these benefits but gain a +1 circumstance bonus to attack rolls and damage. If your rival becomes your ally or a member of your party, you gain the Diehard and save bonus benefits, as long as that's the case.

**Source:** `= this.source` (`= this.source-type`)
