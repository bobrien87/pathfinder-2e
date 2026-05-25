---
type: background
source-type: "Remaster"
traits: ["[[Persona flirt]]"]
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Deception, Shelyn Lore Lore"
feats: "[[Charming Liar]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Receiving attention has always come easily to you, be it because of your good looks, your charming personality, your way with words, or something else entirely, yet you've never really settled down. You spent much of your life up to this point on the road or at sea, traveling from town to town and never staying long enough in one place to ever have a proper home. The reasons for this itinerant lifestyle aren't important, but what is important is that it never took you long to find someone to hold after arriving in a new town. Whether your inevitable departure was heralded by false promises to return or tearful goodbyes, you've left in your wake a mix of pining admirers and jilted lovers. One of these days, you might actually settle down. One of these days, you might find someone you'll want to spend the rest of your life with. One of these days, you might find a place to call home. But today is not that day.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Deception skill and the Shelyn Lore skill. You gain the [[Charming Liar]] skill feat.

If you have the Flirt persona trait, you also become trained in the Sailing Lore skill.

**Source:** `= this.source` (`= this.source-type`)
