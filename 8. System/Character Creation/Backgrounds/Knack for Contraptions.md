---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Engineering Lore Lore"
source: "Pathfinder Shades of Blood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've always liked to fiddle with things mechanical, anything from simple tools to more complex contraptions. The more parts, especially moving parts, the better. You often got in trouble as a child for dismantling something just to see how it worked. As you grew up, you drew plans and yearned to study engineering so that you could build something of your own. You read tales of Jistkan marvels, Shory flying cities, and Azlanti magitech and clockworks. After hearing that an expedition to old Azlant was looking to take on research assistants, you immediately signed up, hoping for a chance to study the ruins. You've even heard that the town has a business with a clockwork soldier working as a guard! You've spent the whole ship ride over to Talmandor's Bounty thinking of the wonders you might find.

Choose two attribute boosts. One must be to **Intelligence** or **Dexterity**, and one is a free attribute boost.

You're trained in the Crafting skill and the Engineering Lore skill. You can cast [[Live Wire]] as an arcane innate cantrip. As normal, the cantrip heightens to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
