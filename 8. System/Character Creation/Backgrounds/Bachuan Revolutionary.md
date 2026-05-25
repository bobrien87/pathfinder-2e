---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Law Lore Lore"
feats: "[[Sign Language]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

**Access** Bachuan origin

Your heart yearns for change and burns for your people. You refuse to conform to the laws that bind you, so you rebel in flashy ways. Your hair is either shaved or grown wild and loose. Your clothes don't conform to Bachuan's society, often cut out in garish shapes and dyed in vivid colors. Your call for change is a dire battle, and not every rebellion is well equipped. Whether you choose to fight another day or bring your cause on your adventures, that's up to you.

Choose two attribute boosts. One must be to **Wisdom** or **Strength**, and one is a free attribute boost.

You're trained in Society and Law Lore. You gain the Sign Language skill feat.

**Source:** `= this.source` (`= this.source-type`)
