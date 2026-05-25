---
type: background
source-type: "Remaster"
boosts: "Int/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Through bloody combat, a terrible accident, or purposeful sacrifice, you've lost some piece of your body that has been replaced with a clockwork mechanism. Whether your arm is now a whirring series of pumps, steel coils, and iron gears; your heart a intricate crystal clock that requires winding every day; or your lower leg a sculpted metal tube powered by adamantine springs and steam, part of you needs regular maintenance and repair. You might have received instructions from the brilliant inventor who saved you, or you might have woken up on a battlefield with no memory of the procedure or the individuals involved. Regardless, you possess the knowledge to take care of yourself-even if it's how to wind a key in your own heart or reconstruct a mechanical foot.

Choose two attribute boosts. One must be to **Strength** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill. Every day you must perform 10 minutes of maintenance and wind up your clockwork parts, or you risk failure of the components, with consequences depending on what you replaced (determined by you and the GM). Your clockwork components allow you to react to danger with alacrity. You gain a +2 circumstance bonus to initiative rolls.

**Source:** `= this.source` (`= this.source-type`)
