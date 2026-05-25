---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Backswing]]", "[[Earth]]", "[[Magical]]", "[[Shove]]"]
price: "{'gp': 325}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Embedded along the length of this *+1 striking greatclub* are the teeth and scales of a zetogeki, a giant lizard that can absorb and then release bursts of kinetic energy. The more momentum a wielder builds up while swinging the weapon, the more forceful the impact when it finally makes contact.

**Activate—Store Kinetic Energy** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** You add a circumstance bonus to your attack with the *kinetic club's* backswing trait and successfully Strike your target

**Effect** You channel the club's stored energy into the Strike, dealing 1d6 additional damage. If the club has a *greater striking* rune, increase the additional damage to 2d6. If the club has a *major striking* rune, increase the additional damage to 3d6.

**Source:** `= this.source` (`= this.source-type`)
