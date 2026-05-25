---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Magical]]", "[[Mythic]]"]
price: "{'gp': 240}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When empty, the *vortex pouch*'s net seems too loose to hold much. However, when used to catch the wind, it stretches to hold the air. With nowhere for the wind to go, the air inside it swirls violently. If the caught wind includes a storm, clouds, fog, or similar effect, it's visible among the whirlwind.

**Activate—Catch Wind** `pf2:2` (air, manipulate)

**Requirements** The *vortex pouch* is empty

**Effect** You gather the nearby air and wind within the *vortex pouch*. Creatures within a @Template[type:emanation|distance:20] must attempt a DC 20 [[Fortitude]] save or be moved 5 feet closer toward you as the air rushes into the pouch. Targets that critically fail the save are moved 10 feet. You can Sustain the activation once per round, up to 1 minute, to continue Catching Wind. If you spend a Mythic Point when Catching Wind, the *vortex pouch* gathers air in a 10-mile radius; though the vortex is only strong enough to forcibly suck in creatures within the original @Template[type:emanation|distance:20], weaker creatures with the air trait and creatures associated with the sky in the 10-mile radius will know your general direction and feel a sense of unease, granting you a +2 status bonus to Intimidation checks against those creatures for 1 week. When you end the activation, the *vortex pouch* becomes 1 Bulk and you can empty it using Release Wind.

**Activate—Release Wind** `pf2:2` (air, manipulate)

**Requirements** The *vortex pouch* contains air or wind

**Effect** Wind rushes out of the *vortex pouch* in a @Template[type:cone|distance:30]. All creatures in the cone take @Damage[8d6[bludgeoning]|options:area-damage] damage (DC 20 [[Fortitude]] save). Creatures that fail their saving throw are pushed 5 feet away from you; creatures that critically fail are pushed 10 feet. If the caught wind included weather that might deal a different type of damage, Release Wind deals this damage instead (for instance, dealing electricity damage if it caught a thundercloud or cold damage if it caught a blizzard).

**Source:** `= this.source` (`= this.source-type`)
