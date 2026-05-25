---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy"
feats: "[[Bon Mot]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

There are many reasons for noble blood to abandon their responsibilities. Whether you fled for safety, for love, to sate a spontaneous spark of rebellion, or to escape unbearable expectations, you've left your lavish life behind for one of newfound experiences. However, how prepared you are for a life on the road is something else entirely.

Choose two attribute boosts. One must be to **Charisma** or **Intelligence**, and one is a free attribute boost.

You're trained in Diplomacy, and either Genealogy Lore or Heraldry Lore. You gain the Bon Mot skill feat.

**Source:** `= this.source` (`= this.source-type`)
