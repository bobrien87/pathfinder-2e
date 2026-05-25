---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting"
feats: "[[Specialty Crafting]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're a skilled weaver, crafting your pieces either by hand or by loom. Whether you revere yourself as an artist or not, none can deny the beauty of your craft. However, the life of a weaver isn't the most exciting one, and your fingers itch for an adventure.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in Crafting, and you're trained in Basket Weaving Lore, Tapestry Lore, or Textile Lore. You gain the Specialty Crafting skill feat.

**Source:** `= this.source` (`= this.source-type`)
