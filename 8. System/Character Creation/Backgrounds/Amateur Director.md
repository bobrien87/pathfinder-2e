---
type: background
source-type: "Remaster"
traits: ["[[Persona leader]]"]
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Theater Lore Lore"
feats: "[[Group Impression]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You grew up a child of the theater. Perhaps your parents were actors or directors, or maybe you fell in with a theater crowd at a young age. Perhaps you and your siblings shared a tradition of putting on plays for your parents or, if you were an only child, maybe you directed your toys and stuffed animals in elaborate productions that played out in your mind. Whatever the case, as you grew older, you found that you were most comfortable helping to organize and facilitate the goals and dreams of others—and not just in the role of being a director for a stage production. You've always derived satisfaction from being the one in charge of something and helping others get organized so as to accomplish something significant. Yet for whatever reason, this never quite grew into your job; you've never actually made money directing, or if you have, it was never enough to allow you to abandon your other responsibilities. Still, the experience you've gained at this amateur work has given you some impressive skills and self-confidence.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in the Diplomacy skill and the Theater Lore skill. You gain the [[Group Impression]] skill feat.

If you have the Leader persona trait, you also become trained in the Scribing Lore skill.

**Source:** `= this.source` (`= this.source-type`)
