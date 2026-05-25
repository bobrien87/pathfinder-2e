---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Labor Lore Lore"
feats: "[[Armor Assist]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Was that five shots or six? Maybe it doesn't really matter in the end, because after those nice folks paid for all your drinks, you woke up to find yourself on the lowest rung of the ladder. Whether you're now a crewmate on a ship, a conscript in an army, or something worse, you've nowhere to go but up. This background generally requires buy-in from the entire group to tell a story allowing you to play a character starting their adventuring due to circumstances outside their own control. However, you can also play a character who was once press-ganged and has since escaped that life. If you do, press-ganged doesn't have the uncommon trait, and it has the same mechanical effects either way.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Athletics skill and the Labor Lore skill. You gain the [[Armor Assist]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
