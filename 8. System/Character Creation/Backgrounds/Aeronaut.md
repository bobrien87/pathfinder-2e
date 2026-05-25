---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Piloting Lore Lore"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have mastered the techniques for piloting all manner of airships—balloons, dirigibles, winged vehicles, or something altogether more fantastical. You have developed expertise in using these vehicles for transport, exploration, and battle. You live for the majestic view these vehicles provide high above the fray and can harness the winds that fill the skies.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in the Athletics skill and the Piloting Lore skill. You gain the [[Assurance]] skill feat with Piloting Lore.

**Source:** `= this.source` (`= this.source-type`)
