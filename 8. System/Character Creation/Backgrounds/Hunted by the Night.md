---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Stealth, Vampire Lore Lore"
feats: "[[Dubious Knowledge]]"
source: "Pathfinder Shades of Blood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're being hunted—by a vampire no less! What you did to offend this nocturnal predator hardly matters now. All you know is that when your bandolier of garlic bulbs, holy water, and religious icons failed to deter your pursuer, you had no other choice but to put as much distance between you and them as possible. You set sail for the Andoren colony of Talmandor's Bounty, where you hope a vast ocean and an island known for its sun-filled days will keep you safe.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Stealth skill and the Vampire Lore skill. You gain the [[Dubious Knowledge]] skill feat.

In addition, you begin play ready to protect yourself from your supernatural stalker. You have a religious symbol, a wooden stake and mallet, and a vial of [[Holy Water]].

**Source:** `= this.source` (`= this.source-type`)
