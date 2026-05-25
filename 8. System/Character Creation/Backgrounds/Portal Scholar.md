---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Arcana, Architecture Lore Lore"
feats: "[[Arcane Sense]]"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Candlaron's legacy is one of the strongest elven legacies on Golarion and beyond, for it was he who first created the aiudara—the network of magical portals that link Kyonin to Castrovel and so many other locations across Golarion. Most of these portals are located in the Inner Sea region, where Candlaron spent the majority of his time. Now that he's long gone, the particulars of how to create new aiudara has eluded discovery, causing some elven scholars to believe that there was something unique to Candlaron's mind or soul that allowed for his ability to craft and enchant so many portals throughout different regions and worlds. Even Treerazer himself hasn't cracked that magical code, although not for lack of trying. At least one aiudara, the remote archway known now as Tanglegate, lies deep in his territory. As one of countless scholars of these portals, you've spent much of your time studying Candlaron's techniques, as well as the complex fundamentals of a wide range of teleportation magics and effects. Whether you seek to find a way to build portals of your own, hope to bolster the aiudara network from further tampering from Treerazer, or are simply enthralled by the supernatural rush of vanishing from reality only to reappear in the same instant somewhere else, portals have long fascinated you.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Arcana skill and the Architecture Lore skill. You gain the [[Arcane Sense]] skill feat, and also gain the [[Restorative Teleportation]] reaction.

**Source:** `= this.source` (`= this.source-type`)
