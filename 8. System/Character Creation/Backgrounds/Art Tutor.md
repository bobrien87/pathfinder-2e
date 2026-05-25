---
type: background
source-type: "Remaster"
traits: ["[[Persona scholar]]"]
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Art Lore Lore"
feats: "[[Crafter's Appraisal]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Art has always been important to you. It's likely that you've got a significant talent for creating artwork yourself, but at the very least, you grew up in a home, neighborhood, or city where artwork was freely available for you to enjoy. The first time you met someone who hadn't had this luxury was a shock, and you promised yourself that you would do whatever you could to bring the joy of artwork to places and people unfortunate enough to be bereft of it. Of course, original art isn't always something that can be transported, so you've settled on the next best thing—teaching others about art, art history, and artistic theory. Whether you've made money by teaching others about art or taken it upon yourself to altruistically educate others, the only thing that approaches the feeling of euphoria you receive from admiring or creating a new piece of art is what you gain by spreading this appreciation to others.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Art Lore skill. You gain the [[Crafter's Appraisal]] feat.

If you have the Scholar persona trait, you also become trained in the Academia Lore skill.

**Source:** `= this.source` (`= this.source-type`)
