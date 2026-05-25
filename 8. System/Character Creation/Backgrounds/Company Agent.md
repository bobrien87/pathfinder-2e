---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Deception, Accounting Lore Lore"
feats: "[[Charming Liar]]"
source: "Pathfinder Shades of Blood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

When the Bountiful Venture Company first invested in the colony of Talmandor's Bounty, the backers expected to see a return on their investment. Nearly a decade later, the Company has yet to realize any profits, and so they've sent you to Ancorato to see what might be done to remedy the situation. Your employers place much of the blame on the colony's governor, Ramona Avandth, whose stubborn refusal to accelerate the investors' repayment schedule has kept the Company from the money it's rightfully due. While several of the Company's representatives—including your direct superior, Verner Tracewell—have already landed on the island, you're to serve in a more unofficial capacity, scouring the colony for mismanagement in hopes Ramona will be unseated from her position and replaced by someone more amenable to the Company's interests.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Deception skill and the Accounting Lore skill. You gain the [[Charming Liar]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
