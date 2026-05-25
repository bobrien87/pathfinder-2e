---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Kaiju Lore Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The lands of Tian Xia can be as dangerous as they are beautiful, and like any land, it calls for hunters. A normal hunter's game varies in size, with the deadliest quarries possessing venomous fangs or a ferocious bite. A monster hunter must be prepared for more supernatural maladies and terrors. As a kaiju stalker, you venture into the Wall of Heaven, Valashmai Jungle, or another land where the bounties are much bigger. A mere scale or feather is your grandest trophy—the survival of your community your ultimate prize.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in Athletics and gain one Athletics skill feat of your choice, best suited toward the style of hunting you prefer.

You're trained in Kaiju Lore. When rolling a Recall Knowledge check using Kaiju Lore and you have sight of one item that belongs to the kaiju you're attempting to Recall Knowledge about, you gain a +1 circumstance bonus to the skill check. The item can range from a scale to slime, to a footprint, or to crafted or harvested goods.

**Source:** `= this.source` (`= this.source-type`)
