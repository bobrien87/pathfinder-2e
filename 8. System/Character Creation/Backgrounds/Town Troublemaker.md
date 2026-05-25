---
type: background
source-type: "Remaster"
traits: ["[[Persona scoundrel]]"]
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery, Underworld Lore Lore"
feats: "[[Dirty Trick]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Every town has at least one of them: the person that everyone "knows" is a bad apple, a rascal, a mixer, or a fly in the ointment—the troublemaker. Your hometown was no exception, because you were that town's troublemaker, or at least one of its more notorious ones! This reputation may not have been warranted—perhaps you took the rap to protect a friend or family member caught in a scandal, or maybe you were tricked or cajoled into a tricky situation by so-called "friends." Or the reputation could be spot-on. Being a town troublemaker doesn't mean you had malice in your heart, of course, especially if the town in question was one ruled by villains or governed by cruelty. One society's troublemaker is, after all, another society's freedom fighter! Regardless of the truth that lies at the heart of your personal situation, your legacy as the town troublemaker has given you great insights into society's seamy underbelly.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in the Thievery skill and the Underworld Lore skill. You gain the Dirty Trick skill feat.

If you have the Scoundrel persona trait, you also become trained in the Norgorber Lore skill.

**Source:** `= this.source` (`= this.source-type`)
