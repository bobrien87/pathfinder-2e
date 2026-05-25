---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're a trained, elegant artist or entertainer for the upper echelon of society. You might be a skilled crafter, a master performer, a highly sought host or companion, an up-andcoming political darling, or a fashionable courtesan, but you've gained the eye of a powerful political patron. Whether it's the pressure of your profession or your patron's expectations, whatever drove you to leave your current life behind for that of a chaotic adventurer's must be worthy of breaking tradition.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in Diplomacy, Performance, or Society. You're trained in a Lore skill of your choice. You gain the Name Drop reaction. At the GM's discretion, you can ask your patron for further assistance and favors, such as monetary or political support. You must keep your patron's favor to avoid losing your benefits; what this entails is between you and the GM but usually implies never publicly speaking or acting against your patron's wishes. If you offend your patron, you lose [[Name Drop]] until you reconcile with them.

**Source:** `= this.source` (`= this.source-type`)
