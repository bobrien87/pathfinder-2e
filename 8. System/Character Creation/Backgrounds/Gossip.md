---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy"
feats: "[[Hobnobber]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Everyone has a nosy auntie, a talkative uncle, or a gossiping relative. Just like them, you don't mind the chatter from the eternal grapevine. Whether you seek out gossip or just happen to be at the right place at the right time, you heard rumors of greater exploits away from the comforts of home. Word gets by, and so should you, so why not give adventuring a try?

Choose two attribute boosts. One must be to **Charisma** or **Intelligence**, and one is a free attribute boost.

You're trained in Diplomacy and a Lore skill of your choice. You gain the Hobnobber skill feat.

**Source:** `= this.source` (`= this.source-type`)
