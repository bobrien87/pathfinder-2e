---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Forest Lore Lore"
feats: "[[No Cause For Alarm]]"
source: "Pathfinder Wardens of Wildwood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You aren't a mere visitor or settler living on a woodland's outskirts; you're an avid inhabitant of the Verduran Forest or another verdant wilderness. Intelligent plants like arboreals and leshies have accepted you as their neighbor, and you're adept at communicating with such creatures to avoid misunderstandings and violence. Even if you aren't part of the Wildwood Lodge, you have such a deeply ingrained connection to nature that the druids welcome you to their event.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Diplomacy skill and the Forest Lore skill. You gain the [[No Cause for Alarm]] skill feat, and you can choose Arboreal as one of your known languages.

**Source:** `= this.source` (`= this.source-type`)
