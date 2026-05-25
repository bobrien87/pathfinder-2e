---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Azlanti Lore Lore"
feats: "[[Multilingual]]"
source: "Pathfinder Shades of Blood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Sure, stargazing is fine and all, but you signed up for the expedition to Ancorato so you could visit the remains of the ancient empire of Azlant. A curious child, you had access to books that covered some of the ancient civilizations that thrived before Earthfall and would often get lost in your own imagination of what life was like way back then. You even managed to learn some ancient languages to further your studies by reading the actual words rather than someone else's translations. You hope that when your contract for Inizkar's expedition finishes, you can start your own expedition into the Azlanti ruins.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Society skill and the Azlanti Lore skill. You gain the [[Multilingual]] skill feat; one language gained must be Azlanti and the other can be any common or uncommon language.

**Source:** `= this.source` (`= this.source-type`)
