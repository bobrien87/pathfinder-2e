---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Arcana"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether you purposefully took it on or had it thrust upon you, a bronze, clockwork object latched onto some part of your body. It may have sunk its needles into you or locked its spidery legs around your neck, torso, or upper arm. Some entity or spirit lives in this collection of gears and wires-whether or not other people hear its whispers is up to you. The entity may be an ancient, terrible being that has razed villages with its hosts, or it may be a brilliant, starry-eyed child who barely understands you're not part of its own body.

You have studied and searched for information on these rare, crab-like machines, leaving you an expert in the binding of elemental spirits or mortal souls to mechanical objects. Though you have several theories on what the symbiotic entity might be, you have no definitive answers-this may be why you're adventuring in the first place, or perhaps you've made a deal with someone to get it removed. The entity might talk to you periodically, or it might only speak when it wants you to do something in particular or finds the two of you in danger. You and the GM should decide on the entity's motivations, or if the motivations should be a secret known only to the GM.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Arcana skill and an additional skill in which the clockwork entity is well-versed, determined by the GM. Any time you attempt a skill check for the entity's skill, the GM can offer you a +1 circumstance bonus to the check, as though the entity were Aiding you. If you accept but fail the check, the entity clenches up and you are [[Stunned]] 1 ([[Stunned]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
