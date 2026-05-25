---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Mercantile Lore Lore"
source: "Pathfinder Revenge of the Runelords Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You hail from a distant land, such as Iblydos or Tian Xia, and you've brought new ways of thinking about the Saga Lands' problems—methods and tactics that have served you well in carving out a heroic legacy that's attracted attention from the region's elite. Your association with the other PCs, your comrades-in-arms, certainly helped bolster your reputation. Queen Sorshen, in particular, has noticed you, and in her invitation to attend the opening ceremonies of the Circle of Open Hands in Xin-Eurythnia, she mentions that she'd like to speak to you about potentially establishing trade agreements with your homeland.

Choose two attribute boosts. One must be to **Charisma** or **Constitution**, and the other is a free attribute boost.

You're trained in Diplomacy and Mercantile Lore. Long journeys invigorate you. When you make your daily preparations after spending the previous day traveling in exploration mode or the first time after using magic to travel a distance of at least 100 miles (or to another plane), your excitement and anticipation about what you might encounter next gives you a +1 status bonus to Will saves for the next 8 hours after your daily preparations.

> [!danger] Effect: Distant Traveler

**Source:** `= this.source` (`= this.source-type`)
