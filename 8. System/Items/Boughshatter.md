---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Earth]]", "[[Magical]]", "[[Poison]]", "[[Versatile p]]"]
price: "{'gp': 2875}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The spikes of this *+2 greater striking standard-grade adamantine morningstar* have a faintly green shimmer, as if resembling Ayrzul's crystalline teeth. The weapon vibrates briefly when first drawn in or carried into a radioactive area, with the intensity of the vibration correlating to the radioactivity's strength. While you carry Boughshatter, you gain a +4 status bonus to saving throws against radiation, including Ayrzul's Blight.

**Activate—Splintering Strike** `pf2:2` (manipulate)

**Frequency** Once per minute

**Effect** Make a Strike with the morningstar that deals an extra die of weapon damage. If you make this Strike against a fungus, plant, or creature with the wood trait, the Strike ignores 10 points of the target's resistances to bludgeoning and piercing damage, if any. By damaging such a creature, the morningstar causes the target's flesh to explode in a shower of splinters that affect a 30-foot cone originating from the target's space, dealing 8d6 piercing damage to creatures in the area (DC 30 [[Reflex]] save). You and the target are unaffected by these splinters.

**Activate—Absorb Corruption** R (concentrate)

**Frequency** Once per day

**Trigger** You take poison or void damage;

**Effect** You channel some of the toxic energy into Boughshatter, granting the weapon the effects of either a [[Decaying]] weapon rune, [[Grievous]] weapon rune, or [[Wounding]] weapon rune for 1 minute. While under this effect, the morningstar glows with dim green light in a 20-foot radius.

**Source:** `= this.source` (`= this.source-type`)
