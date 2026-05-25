---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 650}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking dagger* made of black stone is carved from the bloodstained earth of the Shadefields and carries the grudge of the Shoanti who perished on that battlefield.

**Activate—Vengeful Blood** `pf2:1` (concentrate, emotion, fear, mental, visual)

**Frequency** once per hour

**Effect** Blood seeps out of the knife, coating your hand. Enemies within 30 feet who can see this must succeed at a DC 26 [[Will]] save or become [[Frightened]] 1 (frightened 1 and [[Doomed]] 1 on a critical failure). The knife continues to bleed for 1 minute or until you make a successful Strike with it, which deals an additional 1d6 persistent,bleed damage.

**Source:** `= this.source` (`= this.source-type`)
