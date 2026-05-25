---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While Yaezhing is feared and seldom worshipped in the open, some regions of Tian Xia see him as a god of necessary evil and their only hope for justice. This garment is often worn by bounty hunters or priests of Yaezhing, yet non-worshippers of the god of harsh justice sometimes wear this item without fear of religious persecution. The red cape appears almost black while in the shadows, with a lighter red mandala pattern on it that resembles a shuriken.

When you invest a cape of justice, you must designate a single creature as your offender. You must have met the creature before, or the creature should have a persona well known to the public (for instance, a bandit's name or epithet, if not their face as shown on a wanted poster).

You gain a +1 item bonus to [[Demoralize]] this creature. If you don't designate a creature as your offender when you invest the cape of justice, or if 24 hours pass without you either slaying or capturing your offender, your thoughts become worried and distracted, and you take a –1 item penalty to Perception checks for the next 24 hours.

> [!danger] Effect: Cape of Justice (Distracted)

**Activate—Force Shuriken** `pf2:1` (force, manipulate)

**Frequency** once per hour

**Effect** By using a free hand to grab the edge of your cape and give it a quick flourish, you cause a red, shurikenshaped bolt of force to fire at a target within 60 feet that you can see. The shuriken hits automatically and deals @Damage[(1d4+1)[force]] damage, or @Damage[(2d4+2)[force]] damage if the target is your designated offender. If the target is within 30 feet, you can attempt to [[Demoralize]] the target as a free action after the shuriken strikes them.

**Activate—Enact Justice** `pf2:2` (concentrate, incapacitation, manipulate)

**Frequency** once per day

**Effect** You produce manacles from the cape and then fling them at a Medium or Small bipedal target within 30 feet. The target must attempt a DC 18 [[Reflex]] save.
- **Critical Success** The target is unaffected, and the manacles vanish.
- **Success** The manacles strike the target's legs but fail to latch properly. The target is [[Off Guard]] until the start of your next turn, at which point the manacles vanish.
- **Failure** The manacles lock on the target's legs. The target takes a –15-foot circumstance penalty to its Speeds for 1 minute, or until it Escapes or is freed by someone using Pick a Lock (DC 18), after which the manacles vanish.
- **Critical Failure** As failure, but the target is [[Immobilized]] for as long as the manacles remain in place.

**Source:** `= this.source` (`= this.source-type`)
