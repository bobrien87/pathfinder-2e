---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Magical]]", "[[Nonlethal]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 750}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Three dried tentacles from a giant squid studded with pufferfish spines have been twisted together to form this robust *+1 [[Wounding]] whip*. With a clever flick of the wrist, they can be unfurled into a deadly arc of poisonous barbs.

**Activate—Poison Barrage** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You lash out with the whip's three tentacles in a @Template[cone|distance:15]. Each creature inside the cone must attempt a DC 27 [[Fortitude]] save or take @Damage[4d6[poison]|options:area-damage] damage. On a critical failure, the creature also takes 1d6 persistent,poison damage.

**Craft Requirements** The initial raw materials must include three tentacles from a giant squid.

**Source:** `= this.source` (`= this.source-type`)
