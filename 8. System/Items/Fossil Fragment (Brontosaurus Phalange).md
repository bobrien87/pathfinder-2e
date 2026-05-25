---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Earth]]", "[[Magical]]"]
price: "{'gp': 21000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A fossil fragment is a piece of a fossil creature, typically a smaller bone from a larger specimen.

**Activate—Fossil Metamorphosis** `pf2:2` (concentrate, manipulate)

**Effect** You activate the fragment by placing it on solid ground and then speaking its name, causing the fragment to form the full fossilized skeleton of a creature. In creature form, the fragment has the minion trait. Because it's an animated fossil instead of a living creature, it has the construct and earth traits and lacks its normal creature type trait (typically animal). It's also immune to bleed, death effects, disease, doomed, drained, [[Fatigued]], healing, nonlethal attacks, [[Paralyzed]], poison, sickened, vitality, void, and [[Unconscious]]. It can understand your language, and it obeys you to the best of its ability when you use an action to command it. The specifics of each creature, as well as the activation's frequency, if any, appear in its entry below.

This massive toe bone becomes a [[Brontosaurus]] when activated. It can be called upon no more than four times per month. The skeleton remains for 24 hours if used as a beast of burden or for transport. If it attempts an attack or otherwise engage in combat, it reverts to its fragment form after 1d4 rounds.

The skeleton is so massive and sturdy that it can serve as the base of a structure (from an item or spell effect with the structure trait), provided the structure is no larger than 20 feet in width or height. When the brontosaurus reverts to its fragment form, the structure reverts with it.

**Source:** `= this.source` (`= this.source-type`)
