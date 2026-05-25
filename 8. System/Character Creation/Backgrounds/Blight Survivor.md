---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Nature, Fungus Lore Lore"
feats: "[[Natural Medicine]]"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Centuries ago, the elven witch Silisifex played an important role in the fight against Treerazer. With her deep knowledge, power over primal magic, and abiding faith in Calistria, she was one of the first elves to directly fight against the encroaching fiendish blight that was Tanglebriar. Her discoveries, teachings, and lore have continued to protect and inspire elves to this very day, centuries after she vanished mysteriously on a mission into Tanglebriar back in 3050 ar.

Whether you're a primal spellcaster or merely someone whose life was impacted by Tanglebriar's blight, Silisifex's discoveries and methods for combating the demonic corruption of nature has benefited you significantly over the course of your life and may even have saved you from being corrupted yourself. Alternately, you could have had close friends or family members who became corrupted only to have been restored before that corruption could become permanent. Many have succumbed to the influence of Tanglebriar over the ages, but you count yourself as one of the survivors of this corruption. Using your hard-earned experience to help others survive their encounter with the blight has, in part, defined your role in Kyonin or abroad.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Nature skill and the Fungus Lore skill. You gain the [[Natural Medicine]] skill feat. In addition, once you're 4th level, you gain the ability to cast [[Cleanse Affliction]] as an innate primal spell once per day. This spell automatically heightens to a rank equal to half your level, rounded up. If you're cleansing an affliction with the fungus trait, you gain a +4 status bonus to your counteract check.

**Source:** `= this.source` (`= this.source-type`)
