---
type: background
source-type: "Remaster"
boosts: "Con/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Stealth, Warfare Lore Lore"
feats: "[[Terrain Stalker]]"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Elves are known to be talented and gifted archers. Whether you grew up in elven society or sought one out for training, you've studied the secrets of ranged combat with some of the best teachers elves have to offer. While traditionally these secrets are focused on the practice of archery, you may have instead focused your studies in a different way to maximize and enhance your skills with any number of diverse ranged weapons, from simple ones like slings or javelins to less common weapons like pistols or rifles—or any ranged weapon in between. You didn't stop at learning these secrets for yourself, though—you've spent time traveling the world to bring this lore to other worthy students across the Inner Sea region and beyond. A big part of your lectures and lessons involves stories of famous archers from the past, and one of your favorites is the legendary elven archer Jelarial, who (with her magical bow Wintershot) helped lead a group of elves north into the Crown of the World to escape the coming devastation of Earthfall eons ago. During your travels, you've often had to resort to stealth when traveling through dangerous areas, a skill that also greatly aids your ability to find a hiding spot to lie in wait when hunting prey for food or sniping foes from afar—these tactics too have influenced how you teach your students. Now, though, you've come to Kyonin, be it a return home after your travels or to offer your skills to new students.

Choose two attribute boosts. One must be to **Constitution** or **Dexterity**, and one is a free attribute boost.

You're trained in the Stealth skill and the Warfare Lore skill. You gain the [[Terrain Stalker]] skill feat and have focused your abilities on a specific type of ranged weapon. Choose a ranged weapon (subject to GM approval). For the purposes of proficiency, if your choice is a martial weapon, you treat it as a simple weapon; if it's an advanced weapon, you treat it as a martial weapon. With this weapon, you ignore the penalty for making ranged attacks within your second range increment, and at 5th level, whenever you get a critical hit with this weapon, you get its critical specialization effect.

**Source:** `= this.source` (`= this.source-type`)
