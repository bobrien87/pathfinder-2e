---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Mercantile Lore Lore"
feats: "[[Quick Repair]]"
source: "Pathfinder Triumph of The Tusk Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You belong to a merchant guild, a vendor group, or some other trade organization where you're protected and ensured a fair deal so long as you do what's best for the group's interests. You might be an agent of the Aspis Consortium looking for new opportunities to gain wealth, or you might be a rising merchant eager to prove yourself to your superiors.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Mercantile Lore skill. You gain the [[Quick Repair]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
