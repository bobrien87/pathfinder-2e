---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion, Treerazer Lore Lore"
feats: "[[Quick Identification]]"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Soon after the elves returned to stop Treerazer's corruption of Kyonin, word spread across the globe, reaching the distant elven nation of Jinin in the heart of Tian Xia. No strangers to the fight against evil, a group of Jinin priests and oracles made a desperate pilgrimage across the world to join the fight against Tanglebriar. With them they brought one of their greatest treasures, the legendary staff Fiendbreaker. Created by Jininsiel, founder of Jinin, to serve as a gift to aid the nation's neighbors in Tianjing against their own fiendish invasion, Fiendbreaker's role in helping to defeat Tanglebriar's forces in that ancient war is well known.

Today, with Tanglebriar relatively contained, the need for powerful weapons like Fiendbreaker may be lessened, but this treasured gift's legendary journey across the world is honored still by pilgrimages, during which a group of priests and worshippers from a wide range of faiths gather and carry Fiendbreaker out from Kyonin and back again to honor that legacy. The goal of these journeys isn't to deliver the staff where it's needed. Instead, it's a journey of self-discovery, where the petitioners meditates on Fiendbreaker, the legacy of its creator Jininsiel, and a promise among all pilgrims to stand against the demonic evil.

You have been on at least one of these pilgrimages, and the journey has touched you deeply. You focused your studies on Treerazer, his cult, and his methods, and your long hours studying Fiendbreaker have resulted in a knack for understanding the inner workings of other magic items.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Religion skill and the Treerazer Lore skill. You gain the [[Quick Identification]] skill feat, can use Treerazer Lore checks in place of Perception when you attempt to [[Seek]] or [[Sense the Motive]] of a creature you suspect of being an agent of Treerazer. You also gain the [[Hunt the Razer's Pawn]] action.

**Source:** `= this.source` (`= this.source-type`)
