---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Acrobatics"
feats: "[[Assurance]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You live behind the controls of a vehicle, and can handle anything the road or waves and sky can throw at you. You adventure to test your skills with new and interesting vehicles.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in the Acrobatics skill and either the Driving Lore or Piloting Lore skill. You gain the [[Assurance]] skill feat with the chosen lore.

**Source:** `= this.source` (`= this.source-type`)
