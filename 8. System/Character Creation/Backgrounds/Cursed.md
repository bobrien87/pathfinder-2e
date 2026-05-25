---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Curse Lore Lore"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are the victim of a personal or hereditary curse. Through great effort and occult study, you have learned to fend off the curse's worst effects and, by extension, you can protect yourself against other harmful magic. However, the curse still hangs over you and sometimes manifests in dangerous ways.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You are trained in Occultism and Curse Lore. You gain the [[Warding Sign]] reaction. You and the GM should determine the full effects of the curse, though you've staved most of them off for now. The GM determines the curse's lingering manifestations on you, which usually include at least a constant or very frequent thematic effect and occasional more dangerous effects.

**Source:** `= this.source` (`= this.source-type`)
