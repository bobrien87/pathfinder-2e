---
type: background
source-type: "Remaster"
traits: ["[[Persona guardian]]"]
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Herbalism Lore Lore"
feats: "[[Battle Medicine]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were responsible for caring for someone's needs, be it a sibling or other familial relation, a friend fallen on hard times, or someone who just needed a helping hand at a time when you were there to offer assistance. The satisfaction you get from protecting another, from helping them course-correct from a self-destructive habit, or from assisting them in their recovery from a disaster is more than enough for you, and the idea of being paid for such a service is unsettling and unsavory. When presented with a problem that's beyond your immediate ability to address or resolve, you'll spend days researching methods to provide what help the person needs, either educating yourself on how to provide the aid yourself or by arranging for others to step in to support the person in question.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and the Herbalism Lore skill. You gain the [[Battle Medicine]] skill feat.

If you have the Guardian persona trait, you also become trained in the Library Lore skill.

**Source:** `= this.source` (`= this.source-type`)
