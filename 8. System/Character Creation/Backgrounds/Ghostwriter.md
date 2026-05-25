---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Scribing Lore Lore"
feats: "[[Experienced Professional]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While you enjoy scholastic success, you lack either academic aspirations or academic integrity, and you instead conduct your illicit business of ghostwriting at your school. When desperate students and staff bedeviled by deadlines or quotas seek your services, their academic legitimacy is underpinned by your expertise in ghostwriting and forgery. The Convocation is a treasure trove of new clients and inspirations for someone of your particular skills.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in Society. You're also trained in the Scribing Lore skill or a Lore skill associated with your school. You gain the Experienced Professional skill feat.

**Source:** `= this.source` (`= this.source-type`)
