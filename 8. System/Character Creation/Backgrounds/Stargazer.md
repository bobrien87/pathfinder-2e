---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Astronomy Lore Lore"
source: "Pathfinder Shades of Blood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Ever since you were a child, you've looked up at the night sky and been filled with wonder by the host of celestial bodies that populate the cosmos. Whether you approach your observations from a mystical perspective or through a more scientific lens, when the opportunity to apprentice under the famed astronomer Inizkar presented itself, you booked passage on the first boat to Ancorato. Once you arrive in Talmandor's Bounty, you hope to continue your studies and perhaps even view the heavens from an observatory built by the ancient Azlanti themselves.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in your choice of the Arcana, Nature, or Occultism skill, and gain the [[Assurance]] skill feat in your chosen skill. You're also trained in the Astronomy Lore skill.

In addition, you have an innate sense of time. You can ascertain the time accurate to within the hour even without being able to see the sky.

**Source:** `= this.source` (`= this.source-type`)
