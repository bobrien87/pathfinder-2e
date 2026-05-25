---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Warfare Lore Lore"
feats: "[[Intimidating Glare]]"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

During the first war against Tanglebriar, when the elves returned to Kyonin to fight against Treerazer, many heroes rose to prominence while reclaiming their ancestral homeland from demonic occupation. Some of those heroes' tales are still told today. The legend Kyloss Syndar in particular, whose bravery against Treerazer's minions came to a glorious end as he single-handedly slew the demonic hydra Slithermaw and died of his wounds, has always loomed large in your mind, as you can trace your lineage back through the generations to this storied hero. Whether you carry that link with pride and strive to live up to his legacy or instead have felt hounded by a family history you'd rather leave behind in hopes of building something of your own, the demonic armies of Tanglebriar don't care. Demons live longer than elves, and many who clashed against Kyloss still live today. They have at times made your life difficult, to say the least. Whether you've lived life on the run, lost a family member to demonic attack, or simply endured the frightening sensation of being stalked, Treerazer and his agents believe your bloodline should be wiped out. Your focus in honing your skills in combat, the force of your personality, or simply remaining ready to fight for your life at a moment's notice, have shaped you into an increasingly dangerous foe against demonkind.

Choose two attribute boosts. One must be to **Charisma** or **Strength**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Warfare Lore skill. You gain the Intimidating Glare skill feat. In addition, you gain a +1 circumstance bonus to all saving throws against mental effects. For 1 minute after you witness a demon suffer from having its sin vulnerability triggered, this increases to a +2 circumstance bonus.

> [!danger] Effect: Demon Hunted

**Source:** `= this.source` (`= this.source-type`)
